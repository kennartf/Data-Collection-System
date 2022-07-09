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
login_manager.login_view = 'authent.login'
login_manager.init_app(app)
login_manager.login_message_category = 'info'



from E_data_system.views.routes import view
from E_data_system.staffs.routes import staff_page
from  E_data_system.youthpage.routes import youth
from E_data_system.admin.routes import admin_only
from E_data_system.errors.routes import my_error_page
from E_data_system.accounts.routes import user_account
from E_data_system.authentication.routes import authent
from   E_data_system.image_utils.img_process import pic_utils




app.register_blueprint(view, url_prefix='/')
app.register_blueprint(youth, url_prefix='/')
app.register_blueprint(admin_only, url_prefix='/')
app.register_blueprint(authent, url_prefix='/')
app.register_blueprint(user_account, url_prefix='/')
app.register_blueprint(pic_utils, url_prefix='/')
app.register_blueprint(staff_page, url_prefix='/')
app.register_blueprint(my_error_page, url_prefix='/')

