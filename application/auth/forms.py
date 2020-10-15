from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators
from wtforms.validators import ValidationError, DataRequired, EqualTo
from application.auth.models import User

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3, max=10, message="Username has to contain 3-10 characters")])
    password = PasswordField("Password")
    submit = SubmitField("Create account")

    def validate_username(self, username):
        k = User.query.filter_by(username=username.data).first()
        if k is not None: # if user account already created
            raise ValidationError('Choose another username')

    class Meta:
        csrf = False
