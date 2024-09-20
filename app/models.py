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

    def win_match(self):
        self.wins += 1
    
    def lose_match(self):
        self.losses += 1

    def draw_match(self):
        self.draws += 1

    def score_goals(self, goals):
        self.goals += goals

    def __eq__(self, other):
        return self.name == other.name

    @property
    def points(self):
        return self.wins * 3 + self.draws
    
    @property
    def alternative_points(self):
        return self.wins * 5 + self.draws * 3 + self.losses

    @property
    def rank(self):
        return (-self.points, -self.goals, -self.alternative_points, self.reg_date)
    
    def __repr__(self):
        return f"{self.name}, {self.points} points, {self.goals} goals, " \
            + f"{self.alternative_points} alt points, registered {self.reg_date.strftime(REG_DATE_FORMAT)}"

class Match:
    WIN, DRAW, LOSE = "WIN", "DRAW", "LOSE"

    def __init__(self, home, away, home_goals, away_goals):
        self.home = home
        self.away = away
        self.home_goals = home_goals
        self.away_goals = away_goals

        if self.home_goals > self.away_goals:
            self.home.win_match()
            self.away.lose_match()
        elif self.home_goals < self.away_goals:
            self.home.lose_match()
            self.away.win_match()
        else:
            self.home.draw_match()
            self.away.draw_match()

        self.home.score_goals(self.home_goals)
        self.away.score_goals(self.away_goals)

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
        return f"{self.home} {self.home_goals} - {self.away} {self.away_goals}"


def add_team(team):
    TEAMS[team.name] = team

def add_match(match):
    MATCHES.append(match)

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