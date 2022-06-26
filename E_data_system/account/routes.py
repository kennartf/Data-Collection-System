import imp
from flask import Blueprint
from flask import redirect, render_template, request, flash



account = Blueprint('account', __name__)


@account.route('/account')
def account():
    return render_template('account.html')