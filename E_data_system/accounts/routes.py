from flask import Blueprint
from flask import redirect, render_template, request, flash



user_account = Blueprint('account', __name__)


@user_account.route('/account')
def account():
    return render_template('profile_account.html')