from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    location = StringField('Please enter a location', validators=[DataRequired()])
    submit = SubmitField('Submit')
