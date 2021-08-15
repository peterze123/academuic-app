from flask import Blueprint, redirect, render_template, url_for, flash, session, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, validators, TextAreaField, StringField
from wtforms.fields.html5 import TimeField, DateField, IntegerField

import tasks
from models import Tasks
from app import db
from datetime import datetime

#
bp = Blueprint('tasks', __name__)

# adding tasks for the day, wtForm
class AddForm(FlaskForm):
    title = TextAreaField('Title',
                          [validators.length(max=100), validators.DataRequired(message='Please enter a title')],
                          render_kw={"rows": 1, "cols": 30})
    task = TextAreaField('Description',
                         [validators.length(max = 200), validators.DataRequired(message='Please enter a description')],
                         render_kw = {"rows": 5, "cols": 30})
    date= DateField('Date', format='%Y-%m-%d', default=datetime.now())
    time= TimeField('Time', format='%H:%M', default=datetime.now())
    submit = SubmitField('Create')
    persons= IntegerField(0)
    zoom= StringField()
    hours = IntegerField(0)

# delete tasks 
class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Join')

# after implementing the login functions change 'foo' tp session['name']
@bp.route('/board', methods = ['GET', 'POST'])
def board():
    t = Tasks.query.filter_by(name = 'foo')
    #
    return render_template('my_board.html', t = t, name = 'foo')

@bp.route('/information', methods = ['GET', 'POST'])
def information():
    return render_template('info.html')

@bp.route('/create', methods = ['GET','POST'])
def create():
    form = AddForm()
    #
    if form.validate_on_submit():
        URL = url_for('tasks.board')
        #
        t = Tasks(name = 'foo',
                  content = form.task.data,
                  time = str(form.time.data),
                  date=str(form.date.data),
                  title=form.title.data,
                  numPersons=form.persons.data,
                  numHours=form.hours.data,
                  zoom=form.zoom.data)

        db.session.add(t)
        db.session.commit()
        #
        return redirect(url_for("tasks.information"))
    return render_template('create.html', form = form)




