import os
import sqlite3
from flask import Flask 
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager, LoginManager
from E_data_system.hidden.config import mail_username, mail_password




app = Flask(__name__)


app.config['SQLALchemy_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'fed557ce4beb7dd1f0de8161f14441cc2717524e12054e3b71fd27aa55e5'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] =587
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False 



mail = Mail(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'authen.login'
login_manager.init_app(app)
login_manager.login_message_category = 'info'





