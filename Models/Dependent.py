from DatabaseDriver import db
from datetime import datetime

class Dependent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createdAt= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(20), unique=False, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)


    def __repr__(self):
        return f"id: {self.id}, Name : {self.name}, createdAt: {self.createdAt}"