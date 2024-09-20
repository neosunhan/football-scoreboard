from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import TeamsForm, MatchesForm
from app.parser import parse_teams, parse_matches
from app.models import Team
import sqlalchemy as sa


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    teams_form = TeamsForm()
    matches_form = MatchesForm()
    if teams_form.validate_on_submit():
        teams = parse_teams(teams_form.teams.data)
        for team in teams:
            db.session.add(team)
        db.session.commit()
        flash(f"added teams: {[team for team in teams]}")
        return redirect(url_for("index"))
    if matches_form.validate_on_submit():
        matches = parse_matches(matches_form.matches.data)
        for match in matches:
            db.session.add(match)
        db.session.commit()
        flash(f"added matches: {[match for match in matches]}")
        return redirect(url_for("index"))
    
    groups = {group: db.session.scalars(sa.select(Team).filter_by(group=group)).all() for group in range(1, 3)}
    return render_template('index.html', groups=groups, teams_form=teams_form, matches_form=matches_form)
