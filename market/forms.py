from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label="User Name:", validators=[Length(min=2, max=32), DataRequired()])
    email = StringField(label="Email Address:", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password:", validators=[Length(min=8, max=32), DataRequired()])
    password2 = PasswordField(label="Confirm Password:",
                              validators=[Length(min=8, max=32), EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Create Account")

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
