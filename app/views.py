from app import app,db
from flask import render_template, request, redirect, url_for, flash
from app.models import Doctor, Patient, Dose

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/register_doctors', methods=['POST'])
def register_doctor():
    form = request.form
    doctor = Doctor(
        name =form['name'], 
        email =form['email_address'], 
        password = form['password'])
        #id = form['id_number'])
    doctor.set_password(form['password'])
    db.session.add(doctor)
    db.session.commit()
    return 'Doctor registered'

@app.route('/login_doctors', methods=['POST'])
def login_doctor():
    form = request.form
    doctor = Doctor.query.filter_by(email=form['email_address']).first()
    if doctor.check_password(form['password']):
        return redirect(url_for('patients'))
    else:
        return 'Invalid login'
@app.route('/patients', methods=['POST','GET'])
def patients():
    return 'Successfully registered'