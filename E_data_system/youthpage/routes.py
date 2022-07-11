import imp
from flask import Blueprint, render_template
from flask_login import login_required


youth = Blueprint('youth', __name__)



@youth.route('/ythdashbord')
def ythdashbord():
    # login_required()
    
    return render_template('youthpage.html')