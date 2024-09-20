TEAMS = {}
MATCHES = []

class Team:
    def __init__(self, name, registration_date, group):
        self.name = name
        self.reg_date = registration_date
        self.group = group
        self.matches = []


class Match:
    def __init__(self, home, away, home_goals, away_goals):
        self.home = home
        self.away = away
        self.home_goals = home_goals
        self.away_goals = away_goals