from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

#UPLOAD FOLDER
UPLOAD_FOLDER = "./app/static/uploads"

#SQLALCHEMY DB
SQLALCHEMY_DATABASE_URI = "postgresql://postgresr:postgresr@localhost/"
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(__name__)

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from app import views, models