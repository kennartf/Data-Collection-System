import os
import sqlite3
from flask import Flask 
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager, LoginManager
from E_data_system.hidden.config import mail_username, mail_password


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///record.db'
app.config['SECRET_KEY'] = 'd6ac11bed59b75a6bmn4310nvbv4454ab'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
SECRET_KEY = 'development key'
app.config.from_object(__name__)

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
# login_manager.login_view = 'admin_.login'
login_manager.login_view = 'youth.ylogin'
login_manager.init_app(app)
login_manager.login_message_category = 'info'



from E_data_system.views.routes import view
from E_data_system.admin.routes import admin_
from  E_data_system.youthpage.routes import youth
from E_data_system.errors.routes import my_error_page
from E_data_system.accounts.routes import user_account
from   E_data_system.image_utils.img_process import pic_utils



app.register_blueprint(view, url_prefix='/')
app.register_blueprint(youth, url_prefix='/')
app.register_blueprint(admin_, url_prefix='/')
app.register_blueprint(pic_utils, url_prefix='/')
app.register_blueprint(user_account, url_prefix='/')
app.register_blueprint(my_error_page, url_prefix='/')

