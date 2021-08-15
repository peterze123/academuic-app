from flask import Blueprint, redirect, render_template, url_for, flash, session, request
from courses import cs400, cs570, cs999


bp = Blueprint('course', __name__)

#dummy courses registered bby students
abhishek = [cs400]
course_dict = {'cs400': cs400, 'cs570': cs570, 'cs999': cs999}

@bp.route('/course/', methods=['GET', 'POST'])
def show_courses():
    if request.method == 'POST':
        course_name: str = request.form['course']
        course = course_dict[course_name.lower()]
        abhishek.append(course)
        return redirect(url_for("course.show_courses"))
    else:
        return render_template('profile.html', courses=abhishek)

@bp.route('/deletecourse/<int:course_num>')
def delete_course(course_num: int):
    global abhishek
    for idx, ele in enumerate(abhishek):
        if ele.course_num == course_num:
            abhishek.pop(idx)
            break
    return redirect(url_for("course.show_courses"))