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
    bio = db.Column(db.String(300))
    profile_picture = db.Column(db.String(50), default="dpic001.jpg", unique=True)
    date_joined = db.Column(db.Date, nullable=False)

    def __init__(self, firstname, lastname, gender, email, location, bio, profile_picture):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.bio = bio
        self.profile_picture = profile_picture
        self.date_joined = date.today()

    def __repr__(self):
        return f"<Profile {self.firstname} {self.lastname}>"
