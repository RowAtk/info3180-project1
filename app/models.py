from . import db
from datetime import date

class Profile(db.Model):
    """ DB Model for user profiles """

    pid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    gender = db.Column('gender', db.String(1), db.CheckConstraint("gender in ('M', 'F')"))
    email = db.Column(db.String, unique=True)
    location = db.Column(db.String(50))
    bio = db.Column(db.String())
    profile_picture = db.Column(db.String(), default="default-male.jpg")
    date_joined = db.Column(db.Date, nullable=False)

    def __init__(self, firstname, lastname, gender, email, location, bio):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.bio = bio
        self.date_joined = date.today()

    def set_profile_img(self, profile_picture):
        """ set profile picture (filename) for profile object """
        self.profile_picture = profile_picture

    def __repr__(self):
        return f"<Profile {self.firstname} {self.lastname}>"
