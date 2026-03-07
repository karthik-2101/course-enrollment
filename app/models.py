from app.database import db

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    course = db.relationship('Course', secondary='student_course', back_populates='student')

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    student = db.relationship('Student', secondary='student_course', back_populates='course')

class StudentCourse(db.Model):
    __tablename__ = "student_course"
    student_id = db.Column('student_id', db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), primary_key=True)
    course_id = db.Column('course_id', db.Integer, db.ForeignKey('course.id', ondelete='CASCADE'), primary_key=True)
