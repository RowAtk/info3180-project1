import os
from app import app
from app.models import Profile
from app.forms import ProfileForm 
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename

@app.route("/profile", methods=['GET', 'POST'])
def add_profile():
    """ adding profiles to application """
    pass


@app.route("/profiles", methods=['GET'])
def view_profiles():
    """ viewing all profiles in application """
    pass

@app.route("/profile/<userid>", methods=['GET'])
def view_profile(userid):
    """ view one individual profile """
    pass


# Error handling
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404