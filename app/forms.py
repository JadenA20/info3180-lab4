from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired # For handling file uploads


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

# Exercise 5
class UploadForm(FlaskForm):
        file_upload = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Only images are accepted!')
    ])