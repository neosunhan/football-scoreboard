from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import TeamsForm
from app.parser import parse_teams
from app.models import Team
import sqlalchemy as sa


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # groups = {
    #     1: [
    #         {
    #             "name": "firstTeam",
    #             "registration_date": datetime.datetime(year=2024, month=5, day=17),
    #         },
    #         {
    #             "name": "secondTeam",
    #             "registration_date": datetime.datetime(year=2024, month=2, day=7),
    #         },
    #     ],
    #     2: [
    #         {
    #             "name": "thirdTeam",
    #             "registration_date": datetime.datetime(year=2024, month=4, day=24),
    #         },
    #         {
    #             "name": "fourthTeam",
    #             "registration_date": datetime.datetime(year=2024, month=1, day=24),
    #         },
    #     ]
    # }
    form = TeamsForm()
    if form.validate_on_submit():
        teams = parse_teams(form.teams.data)
        for team in teams:
            db.session.add(team)
        db.session.commit()
        flash(f"added teams: {[team for team in teams]}")
        return redirect(url_for("index"))
    groups = {group: db.session.scalars(sa.select(Team).filter_by(group=group)).all() for group in range(1, 3)}
    return render_template('index.html', groups=groups, form=form)