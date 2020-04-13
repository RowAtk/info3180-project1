from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.file import FileRequired, FileAllowed

nullmsg = "This field is required"

class ProfileForm(FlaskForm):
    """ Form for user profiles """
    firstname = StringField(
        label="Firstname", 
        validators=[
            DataRequired(message=nullmsg),
            Length(min=0, max=30)
        ]
    )
    lastname = StringField(
        label="Lastname", 
        validators=[
            DataRequired(message=nullmsg),
            Length(min=0, max=30)
        ]
    )
    gender = SelectField(
        label="Gender", 
        choices=[
            ('M', "Male"), 
            ('F', "Female")
        ]
    )
    email = StringField(
        label="Email Address", 
        validators=[
            DataRequired(message=nullmsg), 
            Email(message="Invalid Email")
        ]
    )
    location = StringField(label="Location", validators=[DataRequired()])
    bio = TextAreaField(label="Biography", validators=[Length(min=0, max=240)])
    ppicture = FileField(
        label="Profile Picture", 
        validators=[ 
            FileAllowed(
                ['jpg', 'png', 'jpeg'], 
                message="Image Files Only"
            )
        ]
    )
