from flask import Blueprint, redirect, render_template, url_for, flash, session, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, validators, TextAreaField
from wtforms.fields.html5 import TimeField
from models import Tasks
from app import db
from datetime import datetime

#
bp = Blueprint('tasks', __name__)

# adding tasks for the day, wtForm
class AddForm(FlaskForm):
    task = TextAreaField('Task', [validators.length(max = 200), validators.DataRequired(message='please enter a task')], render_kw = {"rows": 5, "cols": 30})
    time= TimeField('Time', format='%H:%M', default=datetime.now())
    submit = SubmitField('OK')

# delete tasks 
class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Complete')

# after implementing the login functions change 'foo' tp session['name']
@bp.route('/board', methods = ['GET', 'POST'])
def board():
    t = Tasks.query.filter_by(name = 'foo')
    #
    return render_template('my_board.html', t = t, name = 'foo')

#
@bp.route('/create', methods = ['GET','POST'])
def create():
    form = AddForm()
    #
    if form.validate_on_submit():
        URL = url_for('tasks.board')
        #
        t = Tasks(name = 'foo', content = form.task.data, time = str(form.time.data))
        db.session.add(t)
        db.session.commit()
        #
        return redirect(URL)
    return render_template('create.html', form = form)

# delete function for public board
@bp.route('/<int:id>/delete', methods = ['GET','POST'])
def delete(id):
    task = Tasks.query.get(id)
    form = DeleteTaskForm()
    #
    if form.validate_on_submit:
        db.session.delete(task)
        db.session.commit()
        flash('A Task has been completed !')
        return redirect(url_for('tasks.board'))