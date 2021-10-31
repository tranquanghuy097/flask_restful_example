from flask_testing import TestCase
from apps.app import create_app
from shared import db
from models.students import Student

import json
import unittest

class TestStudents(TestCase):
    student_list = ['John', 'Michael', 'Jack', 'Jill']

    def create_app(self):
        return create_app('config.TestingConfig')

    def setUp(self):
        for student in self.student_list:
            db.session.add(Student(student))
        db.session.commit()

    def test_get(self):
        response = self.client.get('/students')
        self.assertEqual(response.status_code, 200)
        for index in range(0, len(self.student_list)):
            assert self.student_list[index] == response.json[index]["name"]

    def test_post(self):
        data = {'name' : 'Mark'}
        response = self.client.post('/students', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/students')
        name = response.json[len(self.student_list)]["name"]
        assert name == data["name"]

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()