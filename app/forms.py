from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class TeamsForm(FlaskForm):
    teams = TextAreaField('Teams Input', validators=[Length(min=1)])
    submit = SubmitField('Submit Teams')

class MatchesForm(FlaskForm):
    matches = TextAreaField('Matches Input', validators=[Length(min=1)])
    submit = SubmitField('Submit Matches')

class ClearForm(FlaskForm):
    submit = SubmitField('Clear all data')