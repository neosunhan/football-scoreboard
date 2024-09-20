from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import TeamsForm
from app.models import TEAMS, MATCHES
from app.parser import parse_teams
import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    groups = {
        1: [
            {
                "name": "firstTeam",
                "registration_date": datetime.datetime(year=2024, month=5, day=17),
            },
            {
                "name": "secondTeam",
                "registration_date": datetime.datetime(year=2024, month=2, day=7),
            },
        ],
        2: [
            {
                "name": "thirdTeam",
                "registration_date": datetime.datetime(year=2024, month=4, day=24),
            },
            {
                "name": "fourthTeam",
                "registration_date": datetime.datetime(year=2024, month=1, day=24),
            },
        ]
    }
    teams_form = TeamsForm()
    if teams_form.validate_on_submit():
        parse_teams(teams_form.teams.data)
        flash(f"Data: {teams_form.teams.data}")
    return render_template('index.html', teams=TEAMS, teams_form=teams_form)