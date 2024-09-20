import datetime

from app.models import Team, Match, TEAMS, MATCHES

REG_DATE_FORMAT = r"%d/%m"

def parse_teams(teams_str):
    for team_str in teams_str.split('\n'):
        name, reg_date, group = team_str.rsplit(' ', 2)
        reg_date = datetime.datetime.strptime(reg_date, REG_DATE_FORMAT)
        reg_date = reg_date.replace(year=2024)
        group = int(group)
        if group not in TEAMS:
            TEAMS[group] = []
        TEAMS[group].append(Team(name, registration_date=reg_date, group=group))
