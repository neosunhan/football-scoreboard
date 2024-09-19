import datetime
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Team(db.Model):
    name: so.Mapped[str] = so.mapped_column(sa.String(64), primary_key=True)
    registration_date: so.Mapped[datetime.datetime] = so.mapped_column(default=lambda: datetime.datetime.now())
    group: so.Mapped[int] = so.mapped_column()
    # matches: so.WriteOnlyMapped['Match'] = so.relationship(back_populates='team')

    def __repr__(self):
        return f"Team {self.name}, Group {self.group}, Registered on {self.registration_date}"
    
class Match(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    team_a: so.Mapped[str] = so.mapped_column(sa.ForeignKey(Team.name))
    team_b: so.Mapped[str] = so.mapped_column(sa.ForeignKey(Team.name))
    goals_a: so.Mapped[int] = so.mapped_column()
    goals_b: so.Mapped[int] = so.mapped_column()
    # team: so.Mapped[Team] = so.relationship(back_populates='matches')

    def __repr__(self):
        return f"{self.team_a} {self.goals_a} - {self.team_b} {self.goals_b}"
