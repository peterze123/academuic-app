from models import Users
from flask import Blueprint, url_for, redirect, render_template, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, validators
from app import db

# initializing the blueprint
bp = Blueprint('login', __name__)

#wtform class, form used for sign up and login 
class login(FlaskForm):
    name = StringField('User Name', [validators.DataRequired(message='please enter a name')])
    password = IntegerField('Password', [validators.DataRequired(message="please enter a password")])
    submit = SubmitField('OK')

# login page, search for name in the db
@bp.route('/login', methods=('GET','POST'))
def index():
    form = login()
    if form.validate_on_submit():
        login_user = Users.query.filter_by(user_name = form.name.data).first()
        if login_user is not None:
            password = login_user.password
            if password is not None:
                session['id'] = login_user.id;
                return redirect(url_for('schedule.board'))
            else:
                flash('wrong password!')
        else:
            print(1)
            flash('wrong username!')
    return render_template('login.html', form = form)
