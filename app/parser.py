import datetime

from app.models import Team, Match, get_team

REG_DATE_FORMAT = r"%d/%m"

def parse_add_teams(teams_str):
    teams = []
    for team_str in teams_str.split('\n'):
        if len(team_str.strip()) == 0:
            continue
        name, reg_date, group = team_str.split()
        reg_date = datetime.datetime.strptime(reg_date, REG_DATE_FORMAT)
        reg_date = reg_date.replace(year=2024)
        group = int(group)
        teams.append(Team(name, registration_date=reg_date, group=group))
    return teams

def parse_add_matches(matches_str):
    matches = []
    for match_str in matches_str.split('\n'):
        if len(match_str.strip()) == 0: 
            continue
        home, away, home_goals, away_goals = match_str.split()
        home, away = get_team(home), get_team(away)
        home_goals, away_goals = int(home_goals), int(away_goals)
        matches.append(Match(home=home, away=away, home_goals=home_goals, away_goals=away_goals))
    return matches

def parse_team_name(team_name):
    return get_team(team_name.strip())

def parse_edit_teams(teams_str):
    teams = {}
    for team_str in teams_str.split('\n'):
        if len(team_str.strip()) == 0:
            continue
        old_name, name, reg_date, group = team_str.split()
        reg_date = datetime.datetime.strptime(reg_date, REG_DATE_FORMAT)
        reg_date = reg_date.replace(year=2024)
        group = int(group)
        teams[old_name] = (name, reg_date, group)
    return teams