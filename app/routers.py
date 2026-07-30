from flask import Blueprint, request, jsonify
from app.database import db
from app.models import Student, Course, StudentCourse
from app.schemas import students_schema, courses_schema

main_bp = Blueprint('main', __name__)

@main_bp.route('/addstudent', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully!'}), 201

@main_bp.route('/addcourse', methods=['POST'])
def add_course():
    # print("hii")
    data = request.get_json()
    new_course = Course(name=data['name'])
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message': 'Course added successfully!'}), 201

@main_bp.route('/addstudentcourse', methods=['POST'])
def add_student_course():
    data = request.get_json()
    student_course = StudentCourse(student_id=data['student_id'], course_id=data['course_id'])
    db.session.add(student_course)
    db.session.commit()
    return jsonify({'message': 'Student Course added successfully!'}), 201

@main_bp.route('/getstudents', methods=['GET'])
def get_students():
    list_students = Student.query.all()
    return students_schema.dump(list_students), 200

@main_bp.route('/getcourses', methods=['GET'])
def get_courses():
    list_courses = Course.query.all()
    return courses_schema.dump(list_courses), 200

@main_bp.route('/getcoursebystudent/<id>', methods=['GET'])
def get_course_by_student(id):
    student_obj = Student.query.get(id)
    course = student_obj.course
    return students_schema.dump(course), 200

@main_bp.route('/getstudentbycourse/<id>', methods=['GET'])
def get_student_by_course(id):
    course_obj = Course.query.get(id)
    student = course_obj.student
    return courses_schema.dump(student), 200

@main_bp.route('/updatestudent/<id>', methods=['PUT'])
def update_student(id):
    student_obj = Student.query.get(id)
    print("Hiii>>>", student_obj)
    if student_obj:
        data = request.get_json()
        student_obj.name = data['name']
        student_obj.email = data['email']
        db.session.commit()
        return jsonify({'message': 'Student updated successfully!'}), 200
    else:
        return jsonify({'message': 'No Student found!'}), 404

@main_bp.route('/deletestudent/<id>', methods=['DELETE'])
def delete_student(id):
    student_obj = Student.query.get(id)
    if student_obj:
        db.session.delete(student_obj)
        db.session.commit()
        return jsonify({'message': 'Student deleted successfully!'}), 200
    
@main_bp.route('/deletecourse/<id>', methods=['DELETE'])
def delete_course(id):
    course_obj = Course.query.get(id)
    if course_obj:
        db.session.delete(course_obj)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully!'}), 200
        



