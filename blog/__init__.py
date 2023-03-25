import os

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
engine = create_engine('sqlite:///' + os.path.join(basedir, 'database.db'), echo=True)

Base = declarative_base()

from blog import db
Base.metadata.create_all(engine)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



#
