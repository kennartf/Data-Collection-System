from flask import Blueprint
from flask_mail import Message
from E_data_system .models import User
from E_data_system import db, bcrypt, mail
from .form import RegisterForm, LoginForm
from flask import render_template, flash, request, redirect, url_for, request 
from flask_login import login_user, logout_user, current_user, login_required


authent = Blueprint('authent', __name__)



@authent.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data)
        user = User(branch_id=form.branch_id.data, username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully {user.email}', category='success')
        return redirect(url_for('authent.login'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Registration unsuccesfull {err_msg}', category='error')
    return render_template('signup.html', form=form)



@authent.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(branch_id=form.branch_id.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Logged in as {user.branch_id}')
            return redirect(url_for('youth.ythdashbord'))
        else:
            flash(f'Login uncessful! check email & password', category='error')
    return render_template('login.html', form=form)



@authent.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('view.home'))