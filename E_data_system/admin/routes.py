from flask import Blueprint
from E_data_system import db, bcrypt
from E_data_system.models import User, AdminSession
from .form import ARegisterForm, ALoginForm
from flask import url_for, request, redirect, render_template, flash
from flask_login import login_required, login_user, logout_user, current_user



admin_= Blueprint('admin_', __name__)


@admin_.route('/staff')
@login_required
def staff():
    return render_template('admin_page.html')


@admin_.route('/signup', methods=['GET', 'POST'])
def signup():
    form = ARegisterForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data)
        user = AdminSession(branch_id=form.branch_id.data, email=form.email.data, password=hashed_pwd, is_admin=True)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully {user.email}', category='success')
        return redirect(url_for('admin_.login'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Registration unsuccesfull {err_msg}', category='error')
    return render_template('adminsign.html', form=form)



@admin_.route('/login', methods=['GET', 'POST'])
def login():
    form = ALoginForm()
    if form.validate_on_submit():
        user = AdminSession.query.filter_by(branch_id=form.branch_id.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Logged in as {user.branch_id}')
            return redirect(url_for('admin.index'))
        else:
            flash(f'Login uncessful! check email & password', category='error')
    return render_template('adminlog.html', form=form)



@admin_.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('view.home'))