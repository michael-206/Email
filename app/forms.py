from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    email = StringField('You New Email')
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class SendForm(FlaskForm):
    to = StringField('To', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    body = StringField('Email Body', validators=[DataRequired()])
    submit = SubmitField('Send')