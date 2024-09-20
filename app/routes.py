from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import TeamsForm, MatchesForm
from app.models import get_groups
from app.parser import parse_teams, parse_matches
import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    teams_form = TeamsForm()
    matches_form = MatchesForm()
    if teams_form.validate_on_submit():
        parse_teams(teams_form.teams.data)
        flash(f"teams: {teams_form.teams.data}")
        redirect(url_for('index'))
    if matches_form.validate_on_submit():
        parse_matches(matches_form.matches.data)
        flash(f"matches: {matches_form.matches.data}")
        redirect(url_for('index'))
    return render_template('index.html', teams=get_groups(), teams_form=teams_form, matches_form=matches_form)