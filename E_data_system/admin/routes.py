from flask import Blueprint
from flask_mail import Message
from flask import get_flashed_messages
from E_data_system import db,mail
from flask import url_for, flash, request, redirect, render_template 
# from E_data_system import db, bcrypt, mail


admin_only = Blueprint('admin', __name__)


@admin_only.route('/admin')
def admin():
    return render_template('admin_page.html')
