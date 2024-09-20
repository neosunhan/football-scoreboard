from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import AddTeamsForm, AddMatchesForm, TeamNameForm, EditTeamsForm
from app.models import get_groups, clear_data, add_team, add_match, get_team_names, edit_team
from app.parser import parse_add_teams, parse_add_matches, parse_team_name, parse_edit_teams

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    groups = get_groups()
    return render_template('index.html', groups=groups)

@app.route('/clear', methods=['POST'])
def clear():
    clear_data()
    app.logger.info("Cleared all teams and matches")
    return redirect(url_for('index'))
    
@app.route('/add_teams', methods=['GET', 'POST'])
def add_teams():
    add_teams_form = AddTeamsForm()
    if add_teams_form.validate_on_submit():
        teams = parse_add_teams(add_teams_form.teams.data)
        for team in teams:
            add_team(team)
            app.logger.info(f"Added team {team}")
        return redirect(url_for('index'))
    return render_template('add_teams.html', add_teams_form=add_teams_form)
    
@app.route('/add_matches', methods=['GET', 'POST'])
def add_matches():
    add_matches_form = AddMatchesForm()
    if add_matches_form.validate_on_submit():
        matches = parse_add_matches(add_matches_form.matches.data)
        for match in matches:
            add_match(match)
            app.logger.info(f"Added match {match}")
        return redirect(url_for('index'))
    return render_template('add_matches.html', add_matches_form=add_matches_form)

@app.route('/team_details', methods=['GET', 'POST'])
def team_details():
    team_name_form = TeamNameForm()
    team = None
    if team_name_form.validate_on_submit():
        team = parse_team_name(team_name_form.team.data)
    return render_template('team_details.html', team_names=get_team_names(), team_name_form=team_name_form, team=team)

@app.route('/edit_teams', methods=['GET', 'POST'])
def edit_teams():
    edit_teams_form = EditTeamsForm()
    if edit_teams_form.validate_on_submit():
        teams = parse_edit_teams(edit_teams_form.teams.data)
        for team_name, (new_name, reg_date, group) in teams.items():
            team = edit_team(team_name, new_name, reg_date, group)
            app.logger.info(f"Edited team {team_name} to {team}")
        return redirect(url_for('index'))
    return render_template('edit_teams.html', edit_teams_form=edit_teams_form)