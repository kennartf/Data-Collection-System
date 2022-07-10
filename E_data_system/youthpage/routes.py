import imp
from flask import Blueprint, render_template


youth = Blueprint('youth', __name__)



@youth.route('/ythdashbord')
def ythdashbord():
    
    return render_template('youthpage.html')