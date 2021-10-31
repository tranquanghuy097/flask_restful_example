from flask import Blueprint
from flask_restful import Api, Resource
from models.students import Student

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class StudentListResource(Resource):
    def get(self):
        students = Student.query.all()
        return [Student.serialize(student) for student in students], 200

api.add_resource(StudentListResource, '/students')


