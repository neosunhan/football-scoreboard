from app.models import Team, Match
import datetime

REG_DATE_FORMAT = r"%d/%m"

def parse_teams(teams_str):
    teams = []
    for team_str in teams_str.split('\n'):
        name, reg_date, group_num = team_str.split()
        reg_date = datetime.datetime.strptime(reg_date, REG_DATE_FORMAT)
        reg_date = reg_date.replace(year=2024)
        group_num = int(group_num)
        teams.append(Team(name=name, registration_date=reg_date, group=group_num))
    return teams
