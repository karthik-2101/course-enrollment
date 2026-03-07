from app.models import Student, Course
from app.database import ma

class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)