from flask.globals import request
from models import Schedule
from courses import Course
from course_page import abhishek
from flask import Blueprint, redirect, render_template, url_for

# initializing the blueprint
bp = Blueprint('schedule', __name__)

# schedule for a course
@bp.route('/40000/schedule', methods = ['GET', 'POST'])
def board():
    course_num = int(request.args.get('course'))
    course = Course('Database Management', 40000)
    for i in abhishek:
        if i.course_num == course_num:
            course = i
            break
    

    print('HELLO')
    work = Schedule.query.filter_by(courseId = 40000)
    if len(course.schedules) < 1: course.schedules = work
    return render_template('schedules.html', work = course.schedules, name = course.name)
