from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__,instance_relative_config=True)
app.config['SECRET_KEY'] = '5611222abc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vaccine_new.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import views
from app import models
app.config.from_object('config')

