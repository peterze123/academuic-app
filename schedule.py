from models import Schedule
from flask import Blueprint, redirect, render_template, url_for

# initializing the blueprint
bp = Blueprint('schedule', __name__)

# schedule for a course
@bp.route('/40000/schedule', methods = ['GET', 'POST'])
def board():
    work = Schedule.query.filter_by(courseId = 40000)
    #
    return render_template('schedules.html', work = work, name = 'CS400: Database Management')
