from flask import Flask, request
from flask.templating import render_template
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from courses import Course, Schedule, cs400, cs570, cs999

# initializes the appp
app = Flask(__name__, instance_relative_config = True)
# sets default configurations
app.config.from_mapping(
    # should be overriden in deployment
    SECRET_KEY = 'dev',
    # no host, so I just put the db within the folder
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
)

# initing the database
db = SQLAlchemy(app)

# applying the blueprints
import tasks, login, schedule
app.register_blueprint(login.bp)
app.register_blueprint(schedule.bp)
app.register_blueprint(tasks.bp)

app.add_url_rule('/', endpoint = 'login.index')

#dummy courses registered bby students
abhishek = [cs400]
course_dict = {'cs400': cs400, 'cs570': cs570, 'cs999': cs999}

@app.route('/course/', methods=['GET', 'POST'])
def show_courses():
    if request.method == 'POST':
        course_name: str = request.form['course']
        course = course_dict[course_name.lower()]
        abhishek.append(course)
        return redirect('/course/')
    else:
        return render_template('profile.html', courses=abhishek)


#main
if __name__== '__main__':
    app.run(debug = True)