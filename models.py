from app import db
import datetime
import os

# user db, user_name, password
class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String(20), nullable=False, unique=True)

# task db, content, time, for study session
class Tasks(db.Model):
    __tablename__ = 'Tasks'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    content = db.Column(db.String(200), nullable = False)
    time = db.Column(db.String(), nullable = False)
    date = db.Column(db.String(), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    zoom=db.Column(db.String(150), nullable = False)
    numPersons=db.Column(db.Integer, primary_key=False)
    numHours=db.Column(db.Integer, primary_key=False)
    

# courses db
class Schedule(db.Model):
    __tablename__= 'Schedule'
    id = db.Column(db.Integer, primary_key = True)
    courseId = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String(40), nullable = False)
    date = db.Column(db.String(), nullable = False)
    
# initing the db
def init_db():
    # checking if data.db exists
    if os.path.isfile('data.db'):
        pass
    else:
        open('data.db','a').close();
    db.drop_all()
    db.create_all()

    # push sample students
    student = Users(id = 1, user_name = 'Abhishek', password = 12345, name='Abhishek Shrinivasan')
    db.session.add(student)

    student = Users(id = 2, user_name = 'Shu', password = 12345, name='Shu Gao')
    db.session.add(student)

    student = Users(id = 3, user_name = 'Peter', password = 12345, name='Peter Ze')
    db.session.add(student)

    #push sample schedule
    hw1 = Schedule(courseId = 40000, name='Homework 1', date=str(datetime.datetime(2021, 8, 25, 23, 59, 59)))
    db.session.add(hw1)
    hw2 = Schedule(courseId = 40000, name='Homework 2', date=str(datetime.datetime(2021, 9, 15, 23, 59, 59)))
    db.session.add(hw2)
    midterm = Schedule(courseId = 40000, name='Midterm Exam', date=str(datetime.datetime(2021, 10, 5, 23, 59, 59)))
    db.session.add(midterm)
    hw3 = Schedule(courseId = 40000, name='Homework 3', date=str(datetime.datetime(2021, 10, 26, 23, 59, 59)))
    db.session.add(hw3)
    hw4 = Schedule(courseId = 40000, name='Homework 4', date=str(datetime.datetime(2021, 11, 15, 23, 59, 59)))
    db.session.add(hw4)
    fin_ex = Schedule(courseId = 40000, name='Final Exam', date=str(datetime.datetime(2021, 12, 5, 23, 59, 59)))
    db.session.add(fin_ex)
    db.session.commit()


init_db()