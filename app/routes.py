from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import TeamsForm, MatchesForm
from app.models import get_groups, clear_data, add_team, add_match
from app.parser import parse_teams, parse_matches

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    groups = get_groups()
    return render_template('index.html', teams=groups)

@app.route('/clear', methods=['POST'])
def clear():
    clear_data()
    app.logger.info("Cleared all teams and matches")
    return redirect(url_for('index'))
    
@app.route('/add_teams', methods=['GET', 'POST'])
def add_teams():
    teams_form = TeamsForm()
    if teams_form.validate_on_submit():
        # flash(f"teams: {teams_form.teams.data}")
        teams = parse_teams(teams_form.teams.data)
        for team in teams:
            add_team(team)
            app.logger.info(f"Added team {team}")
        return redirect(url_for('index'))
    return render_template('add_teams.html', teams_form=teams_form)
    
@app.route('/add_matches', methods=['GET', 'POST'])
def add_matches():
    matches_form = MatchesForm()
    if matches_form.validate_on_submit():
        # flash(f"matches: {matches_form.matches.data}")
        matches = parse_matches(matches_form.matches.data)
        for match in matches:
            add_match(match)
            app.logger.info(f"Added match {match}")
        return redirect(url_for('index'))
    return render_template('add_matches.html', matches_form=matches_form)