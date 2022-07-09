
from flask import Blueprint
# from flask_login import login_user, current_user
from E_data_system .models import User 
from flask import Blueprint, render_template, flash, url_for, request, redirect


view = Blueprint('view', __name__)

@view.route('/')
@view.route('/home')
def home():
    return render_template('home.html')

