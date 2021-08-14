from app import db
import os

# # after implementing the login function
# # user db, user_name, password
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     user_name = db.Column(db.String(20), nullable = False, unique = True)
#     password = db.Column(db.Integer, nullable = False)

# task db, content, time
class Tasks(db.Model):
    __tablename__ = 'Tasks'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    content = db.Column(db.String(200), nullable = False)
    time = db.Column(db.String(), nullable = False)
    
    def __repr__(self):
        return f'{self.content} to be completed on {self.time}'

# initing the db
def init_db():
    # checking if data.db exists
    if os.path.isfile('data.db'):
        pass
    else:
        open('data.db','a').close();

    db.drop_all()
    db.create_all()

init_db()