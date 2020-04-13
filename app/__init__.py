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
SQLALCHEMY_DATABASE_URI = "postgresql://postgresr:postgresr@localhost/info_project1"
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config.from_object(__name__)

db = SQLAlchemy(app)
# csrf = CSRFProtect(app)

from app import views, models