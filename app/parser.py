import datetime

from app.models import Team, Match, TEAMS, MATCHES

REG_DATE_FORMAT = r"%d/%m"

def parse_teams(teams_str):
    if not teams_str:
        return
    for team_str in teams_str.split('\n'):
        if len(team_str.strip()) == 0:
            continue
        name, reg_date, group = team_str.split()
        reg_date = datetime.datetime.strptime(reg_date, REG_DATE_FORMAT)
        reg_date = reg_date.replace(year=2024)
        group = int(group)
        TEAMS[name] = Team(name, registration_date=reg_date, group=group)

def parse_matches(matches_str):
    if not matches_str:
        return
    for match_str in matches_str.split('\n'):
        if len(match_str.strip()) == 0: 
            continue
        home, away, home_goals, away_goals = match_str.split()
        home, away = TEAMS[home], TEAMS[away]
        home_goals, away_goals = int(home_goals), int(away_goals)
        MATCHES.append(Match(home=home, away=away, home_goals=home_goals, away_goals=away_goals))