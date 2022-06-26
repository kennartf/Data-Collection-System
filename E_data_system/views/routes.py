
from flask import Blueprint
from flask import Blueprint, render_template, flash, url_for, request, redirect


view = Blueprint('view', __name__)


@view.route('/home')
def home():
    return render_template('home.html')