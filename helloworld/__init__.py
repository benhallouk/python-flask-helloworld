import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask.ext.moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

basedir = os.path.abspath(os.path.dirname(__file__)) 

app = Flask(__name__)
app.config['SECRET_KEY'] = 's3cr3t'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'helloworld.db')
app.config['DEBUG'] = True

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)

toolbar = DebugToolbarExtension(app)

# moment = Moment(app)

import models
import views