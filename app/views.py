import os
from app import app, db
from app.models import Profile
from app.forms import ProfileForm 
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename

@app.route("/profile", methods=['GET', 'POST'])
def add_profile():
    """ adding profiles to application """

    def process_pimg(id):
        """ process profile image uploads for databse saving """

        img = form.ppicture.data
        if img:
            filename = secure_filename(img.filename)
            if not filename:
                filename = f"default-{id}"
            img.save(os.path.join(app.config['PROFILE_PICTURES'], filename)) # save uploaded profile picture
            return filename
        return "default-male.png" if form.gender.data == 'M' else "default-female.png"

    form = ProfileForm() # WTForm Object

    # POST - Accept form data
    if request.method == "POST" and form.validate_on_submit():
        profile = Profile(
            form.firstname.data,
            form.lastname.data,
            form.gender.data,
            form.email.data,
            form.location.data,
            form.bio.data
            # process_pimg(form.ppicture.data)
        )
        db.session.add(profile)
        print(profile.pid)
        return redirect(url_for('home'))

    # GET - Display prfile form
    return render_template('add-profile.html', form=form)


    
    return render_template('add-profile.html')



@app.route("/", methods=['GET']) # HOME
@app.route("/profiles", methods=['GET'])
def view_profiles():
    """ viewing all profiles in application """

    profiles = []
    profiles = Profile.query.all()
    return render_template('profiles.html', profiles=profiles)

@app.route("/profile/<userid>", methods=['GET'])
def view_profile(userid):
    """ view one individual profile """

    profile = Profile.query.get(userid)
    return render_template('user-profile.html', profile=profile)


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404