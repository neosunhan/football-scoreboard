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

def parse_matches(matches_str):
    matches = []
    for match_str in matches_str.split('\n'):
        home, away, home_goals, away_goals = match_str.split()
        home_goals, away_goals = int(home_goals), int(away_goals)
        matches.append(Match(team_a=home, team_b=away, goals_a=home_goals, goals_b=away_goals))
    return matches