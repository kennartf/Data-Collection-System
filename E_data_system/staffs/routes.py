from flask import Blueprint
from flask import url_for, request, redirect, render_template, flash



staff_page = Blueprint('staff_page', __name__)


@staff_page.route('/staff')
def staff():
    return render_template('staff.html')