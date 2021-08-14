import datetime

class Schedule:
    def __init__(self, name: str, date: datetime.datetime) -> None:
        self.name = name
        self.date = date

class Course:
    def __init__(self, name: str, course_number: int, schedules: list = []) -> None:
        self.name = name
        self.course_num = course_number
        self.schedules = schedules
    
    def add_schedule(self, name: str, date: datetime.datetime) -> Schedule:
        schedule = Schedule(name, date)
        self.schedules.append(schedule)
        self.schedules.sort(key=lambda x: x.date)


hw1 = Schedule(name='Homework 1', date=datetime.datetime(2021, 8, 25))
hw2 = Schedule(name='Homework 2', date=datetime.datetime(2021, 9, 15))
midterm = Schedule(name='Midterm Exam', date=datetime.datetime(2021, 10, 5))
hw3 = Schedule(name='Homework 3', date=datetime.datetime(2021, 10, 26))
hw4 = Schedule(name='Homework 4', date=datetime.datetime(2021, 11, 15))
fin_ex = Schedule(name='Final Exam', date=datetime.datetime(2021, 12, 5))

schedules = [hw1, hw2, midterm, hw3, hw4, fin_ex]

cs400 = Course(name='Database Management', course_number=40000, schedules=schedules)
cs570 = Course(name='Algorithms', course_number=57000, schedules=schedules)
cs999 = Course(name='Hackathon 3.0', course_number=99900, schedules=[hw1, hw2, hw3])

