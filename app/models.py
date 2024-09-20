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

    def add_match(self, match, goals, outcome):
        self.matches.append(match)
        self.goals += goals
        if outcome == Match.WIN:
            self.wins += 1
        elif outcome == Match.LOSE:
            self.losses += 1
        elif outcome == Match.DRAW:
            self.draws += 1

    def remove_match(self, match, goals, outcome):
        self.matches.remove(match)
        self.goals -= goals
        if outcome == Match.WIN:
            self.wins -= 1
        elif outcome == Match.LOSE:
            self.losses -= 1
        elif outcome == Match.DRAW:
            self.draws -= 1

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def set_reg_date(self, reg_date):
        self.reg_date = reg_date

    def get_group(self):
        return self.group
    
    def set_group(self, group):
        self.group = group

    def get_matches(self):
        return self.matches

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
            self.home.add_match(self, self.home_goals, Match.WIN)
            self.away.add_match(self, self.away_goals, Match.LOSE)
        elif self.home_goals < self.away_goals:
            self.home.add_match(self, self.home_goals, Match.LOSE)
            self.away.add_match(self, self.away_goals, Match.WIN)
        else:
            self.home.add_match(self, self.home_goals, Match.DRAW)
            self.away.add_match(self, self.away_goals, Match.DRAW)    

    def delete(self):
        if self.home_goals > self.away_goals:
            self.home.remove_match(self, self.home_goals, Match.WIN)
            self.away.remove_match(self, self.away_goals, Match.LOSE)
        elif self.home_goals < self.away_goals:
            self.home.remove_match(self, self.home_goals, Match.LOSE)
            self.away.remove_match(self, self.away_goals, Match.WIN)
        else:
            self.home.remove_match(self, self.home_goals, Match.DRAW)
            self.away.remove_match(self, self.away_goals, Match.DRAW)

    def __repr__(self):
        return f"{self.home.get_name()} {self.home_goals} - {self.away.get_name()} {self.away_goals}"


def add_team(name, reg_date, group):
    TEAMS[name] = Team(name, reg_date, group)
    return TEAMS[name]

def add_match(home, away, home_goals, away_goals):
    match = Match(get_team(home), get_team(away), home_goals, away_goals)
    MATCHES.append(match)
    return match

def get_team(team_name):
    return TEAMS[team_name]

def edit_team(team_name, new_name, reg_date, group):
    team = get_team(team_name)
    team.set_name(new_name)
    team.set_reg_date(reg_date)
    team.set_group(group)
    return team

def edit_match(match_index, home, away, home_goals, away_goals):
    MATCHES[match_index].delete()
    MATCHES[match_index] = Match(get_team(home), get_team(away), home_goals, away_goals)
    return MATCHES[match_index]

def get_team_names():
    return list(TEAMS.keys())

def get_all_matches():
    return MATCHES

def get_groups():
    group_numbers = set(team.get_group() for team in TEAMS.values())
    groups = {group: [] for group in sorted(group_numbers)}
    for team in TEAMS.values():
        groups[team.get_group()].append(team)
    for group in groups.values():
        group.sort(key=lambda team: team.rank)
    return groups


def clear_data():
    TEAMS.clear()
    MATCHES.clear()