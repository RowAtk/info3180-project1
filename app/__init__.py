import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
# SECRET_KEY = 'Sup3r$3cretkey'
SECRET_KEY = os.urandom(24)

#UPLOAD FOLDER
PROFILE_PICTURES = "./app/static/ppictures"

#SQLALCHEMY DB
# SQLALCHEMY_DATABASE_URI = "postgresql://postgresr:postgresr@localhost/info_project1"
SQLALCHEMY_DATABASE_URI = "postgres://unwpgmakjxuayv:c806d6052253293a980a7fa2b2d143095850ac94241e27075e681f0a514b6849@ec2-52-7-39-178.compute-1.amazonaws.com:5432/d81nclv042osql"
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config.from_object(__name__)

db = SQLAlchemy(app)
# csrf = CSRFProtect(app)

from app import views, models