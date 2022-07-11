
from flask import Blueprint
from E_data_system import db
from E_data_system.models import User
from flask import Blueprint, render_template
from flask_login import login_required, current_user


youth = Blueprint('youth', __name__)



@youth.route('/ythdashbord')
@login_required
def ythdashbord():
    return render_template('youthpage.html')