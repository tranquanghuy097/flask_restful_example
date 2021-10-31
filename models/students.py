from shared import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def serialize(self):
        student_json = {
            'id' : self.id,
            'name' : self.name
        }
        return student_json