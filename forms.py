from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired


class bc_form(FlaskForm):
    pill_name = StringField('Pill name', validators=[DataRequired()])
    submit = SubmitField('find out!')


class feedback_form(FlaskForm):
	pill_name = StringField('Pill name', validators=[DataRequired()])
	happiness = RadioField('Happiness', choices=[( '1', 'Very Negatively'), ('2', 'Negatively'),('3', 'No Effect'), 
												 ('4', 'Positively'), ('5', 'Very Positively')])
	mood = RadioField('Mood', choices=[( '1', 'Very Negatively'), ('2', 'Negatively'),('3', 'No Effect'), 
												 ('4', 'Positively'), ('5', 'Very Positively')])
	libido = RadioField('Libido', choices=[( '1', 'Very Negatively'), ('2', 'Negatively'),('3', 'No Effect'), 
												 ('4', 'Positively'), ('5', 'Very Positively')])
	energy = RadioField('Energy', choices=[( '1', 'Very Negatively'), ('2', 'Negatively'),('3', 'No Effect'), 
												 ('4', 'Positively'), ('5', 'Very Positively')])
	
	outlook = RadioField('Outlook', choices=[( '1', 'Very Negatively'), ('2', 'Negatively'),('3', 'No Effect'), 
												 ('4', 'Positively'), ('5', 'Very Positively')])
	submit = SubmitField('submit!')


class email_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('submit!')