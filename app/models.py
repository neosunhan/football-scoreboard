TEAMS = {}
MATCHES = []

class Team:
    def __init__(self, name, registration_date, group):
        self.name = name
        self.reg_date = registration_date
        self.group = group

class Match:
    def __init__(self, home, away, home_goals, away_goals):
        self.home = home
        self.away = away
        self.home_goals = home_goals
        self.away_goals = away_goals

def get_groups():
    groups = {}
    for team in TEAMS.values():
        if team.group not in groups:
            groups[team.group] = []
        groups[team.group].append(team)
    return groups