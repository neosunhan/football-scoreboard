REG_DATE_FORMAT = r"%d/%m"

TEAMS = {}
MATCHES = []

class Team:
    def __init__(self, name, registration_date, group):
        self.name = name
        self.reg_date = registration_date
        self.group = group
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals = 0
        self.matches = []

    def win_match(self, match, goals):
        self.wins += 1
        self.matches.append(match)
        self.goals += goals
    
    def lose_match(self, match, goals):
        self.losses += 1
        self.matches.append(match)
        self.goals += goals

    def draw_match(self, match, goals):
        self.draws += 1
        self.matches.append(match)
        self.goals += goals

    def get_name(self):
        return self.name

    @property
    def points(self):
        return self.wins * 3 + self.draws
    
    @property
    def alternative_points(self):
        return self.wins * 5 + self.draws * 3 + self.losses

    @property
    def rank(self):
        return (-self.points, -self.goals, -self.alternative_points, self.reg_date)
    
    @property
    def reg_date_formatted(self):
        return self.reg_date.strftime(REG_DATE_FORMAT)
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __repr__(self):
        return f"{self.name}, {self.points} points, {self.goals} goals, " \
            + f"{self.alternative_points} alt points, registered {self.reg_date_formatted}"

class Match:
    WIN, DRAW, LOSE = "WIN", "DRAW", "LOSE"

    def __init__(self, home, away, home_goals, away_goals):
        self.home = home
        self.away = away
        self.home_goals = home_goals
        self.away_goals = away_goals

        if self.home_goals > self.away_goals:
            self.home.win_match(self, self.home_goals)
            self.away.lose_match(self, self.away_goals)
        elif self.home_goals < self.away_goals:
            self.home.lose_match(self, self.home_goals)
            self.away.win_match(self, self.away_goals)
        else:
            self.home.draw_match(self, self.home_goals)
            self.away.draw_match(self, self.away_goals)


    def is_draw(self):
        return self.home_goals == self.away_goals

    @property
    def winner(self):
        if self.home_goals > self.away_goals:
            return self.home
        elif self.home_goals < self.away_goals:
            return self.away

    @property
    def loser(self):
        if self.home_goals > self.away_goals:
            return self.away
        elif self.home_goals < self.away_goals:
            return self.home
        
    def __repr__(self):
        return f"{self.home.get_name()} {self.home_goals} - {self.away.get_name()} {self.away_goals}"


def add_team(team):
    TEAMS[team.name] = team

def add_match(match):
    MATCHES.append(match)

def get_team(team_name):
    return TEAMS[team_name]

def get_team_names():
    return list(TEAMS.keys())

def get_groups():
    group_numbers = set(team.group for team in TEAMS.values())
    groups = {group: [] for group in sorted(group_numbers)}
    for team in TEAMS.values():
        groups[team.group].append(team)
    for group in groups.values():
        group.sort(key=lambda team: team.rank)
    return groups


def clear_data():
    TEAMS.clear()
    MATCHES.clear()