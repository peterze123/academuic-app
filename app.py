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
import tasks, login, schedule, course_page, forum
app.register_blueprint(login.bp)
app.register_blueprint(course_page.bp)
app.register_blueprint(schedule.bp)
app.register_blueprint(tasks.bp)
app.register_blueprint(forum.bp)

app.add_url_rule('/', endpoint = 'login.index')


#main
if __name__== '__main__':
    app.run(debug = True)