from flask import Blueprint, request
from flask_restful import Api, Resource
from models.students import Student
from shared import db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class StudentListResource(Resource):
    def get(self):
        students = Student.query.all()
        return [Student.serialize(student) for student in students]

    def post(self):
        new_student = Student(request.json['name'])
        db.session.add(new_student)
        db.session.commit()

api.add_resource(StudentListResource, '/students')


