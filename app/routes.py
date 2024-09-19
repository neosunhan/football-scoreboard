from flask import render_template
from app import app
import datetime

@app.route('/')
@app.route('/index')
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
    return render_template('index.html', groups=groups)