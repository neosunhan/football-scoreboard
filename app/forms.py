from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class TeamsForm(FlaskForm):
    teams = TextAreaField('Teams Input', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Submit Teams')

class MatchesForm(FlaskForm):
    matches = TextAreaField('Matches Input', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Submit Matches')