from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class TaskForm(FlaskForm):
    name = StringField("Task name")
    done = BooleanField("Done")

    class Meta:
        csrf = False
