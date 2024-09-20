from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, Length

class AddTeamsForm(FlaskForm):
    teams = TextAreaField('Teams Input', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Submit Teams')

class AddMatchesForm(FlaskForm):
    matches = TextAreaField('Matches Input', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Submit Matches')

class TeamNameForm(FlaskForm):
    team = StringField('Team Name', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Show team details')