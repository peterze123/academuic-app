from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
import tasks
app.register_blueprint(tasks.bp)

app.add_url_rule('/', endpoint = 'tasks.board')

#main
if __name__== '__main__':
    app.run(debug = True)