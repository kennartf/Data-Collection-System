
from flask import Blueprint
from E_data_system import bcrypt,db
from E_data_system.models import User
from .form import YRegisterForm,YLoginForm
from flask import render_template, flash, redirect, url_for
from flask_login import login_required,login_user,current_user,logout_user



youth = Blueprint('youth', __name__)



@youth.route('/youthdashboard')
@login_required
def youthdashboard():
    return render_template('youthpage.html')


@youth.route('/ysignup', methods=['GET', 'POST'])
def ysignup():
    form = YRegisterForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data)
        user = User(branch_id=form.branch_id.data, username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully {user.branch_id}', category='success')
        return redirect(url_for('youth.ylogin'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Registration unsuccesfull {err_msg}', category='error')
    return render_template('youthsign.html', form=form)



@youth.route('/ylogin', methods=['GET', 'POST'])
def ylogin():
    form = YLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(branch_id=form.branch_id.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Logged in as {user.branch_id}')
            return redirect(url_for('youth.youthdashboard'))
        else:
            flash(f'Login uncessful! check email & password', category='error')
    return render_template('youthlog2.html', form=form)


@youth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('view.home'))