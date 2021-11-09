from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_ckeditor import CKEditorField

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
    body = CKEditorField('Email Body', validators=[DataRequired()])
    submit = SubmitField('Send')