from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qphfjkiynqxlis:95d6aa744b12f8b87cf23d7f7771c8ea6a5685b8766edd633d81021a9745a141@ec2-54-235-146-51.compute-1.amazonaws.com:5432/d61ve54i41hejr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

UPLOAD_FOLDER ='./app/static/uploads'

# Flask-Login login manager


app.config.from_object(__name__)
from app import views

