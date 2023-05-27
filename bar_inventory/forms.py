from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class BarForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    price = DecimalField('price', places = 2)
    chocolate_quality = StringField('chocolate quality')
    melt_temp = StringField('melt_temp')
    freeze_time = StringField('freeze time')
    height = StringField('height')
    weight = StringField('weight')
    cost_of_production = DecimalField('cost of production', places = 2)
    series = StringField('series')
    dad_joke = StringField('dad joke')
    submit_button = SubmitField()

