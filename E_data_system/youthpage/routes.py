import imp
from flask import Blueprint, render_template


youth = Blueprint('youth', __name__)



@youth.route('/ypage')
def ypage():
    return render_template('youthpage.html')