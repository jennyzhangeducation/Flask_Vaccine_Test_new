from app import db 
from werkzeug.security import generate_password_hash, check_password_hash

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
   
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    address = db.Column(db.String(120))
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __repr__(self):
        return '<Patient %r>' % self.name
class Dose(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    date = db.Column(db.String(80))
    patient = db.relationship('Patient', backref=db.backref('doses', lazy='dynamic'))
    doctor = db.relationship('Doctor', backref=db.backref('doses', lazy='dynamic'))
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date
    def __repr__(self):
        return '<Dose %r>' % self.date