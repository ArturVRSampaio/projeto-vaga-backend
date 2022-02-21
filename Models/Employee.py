from DatabaseDriver import db
from datetime import datetime

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createdAt= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(20), unique=False, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    dependents = db.relationship('Dependent', backref='employee', lazy=True)
    
    def __repr__(self):
        return f"id: {self.id}, Name : {self.name}, createdAt: {self.createdAt}"