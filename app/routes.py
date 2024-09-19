from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import TeamsForm
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
    form = TeamsForm()
    if form.validate_on_submit():
        flash(f"Data: {form.teams.data}")
    return render_template('index.html', groups=groups, form=form)