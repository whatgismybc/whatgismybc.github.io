from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class bc_form(FlaskForm):
    pill_name = StringField('Pill name', validators=[DataRequired()])
    submit = SubmitField('find out!')