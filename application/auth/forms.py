from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Create user account")

    class Meta:
        csrf = False
