from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileRequired, FileAllowed

nullmsg = "This field is required"

class ProfileForm(FlaskForm):
    """ Form for user profiles """
    firstname = StringField(label="Firstname", validators=[DataRequired(message=nullmsg)])
    lastname = StringField(label="Lastname", validators=[DataRequired(message=nullmsg)])
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
    bio = TextAreaField(label="Biography", validators=[])
    ppicture = FileField(
        label="Profile Picture", 
        validators=[ 
            FileAllowed(
                ['jpg', 'png', 'jpeg'], 
                message="Image Files Only"
            )
        ]
    )
