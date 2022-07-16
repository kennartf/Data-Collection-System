from flask_wtf import FlaskForm
from flask_login import current_user
from E_data_system .models import User
from flask_wtf.file import FileField, FileAllowed
from wtforms. validators import Email, EqualTo, Length, ValidationError, DataRequired
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField, BooleanField



class ARegisterForm(FlaskForm):
    branch_id = StringField(validators=[DataRequired(), Length(min=1, max=20)],  
                            render_kw={'placeholder': 'Branch id'})
    email = StringField(validators=[DataRequired(), Email()], render_kw={'placeholder': 'email address'})
    password = PasswordField(validators=[DataRequired(), Length(min=1, max=20)], 
                            render_kw={'placeholder': 'Password (at least 3-20 char)'})
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password')], 
                            render_kw={'placeholder': 'Confirm_Password'})
    submit = SubmitField(label='Sign Up')


    def validate_index(self, branch_id):
        user = User.query.filter_by(branch_id= branch_id.data).first()
        if user:
            raise ValidationError('Branch_id already exist! try a different one.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already exist Please choose different one')



class ALoginForm(FlaskForm):
    branch_id = StringField(validators=[DataRequired()], render_kw={'placeholder': 'Branch id'})
    password = PasswordField(validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    remember = BooleanField(label='Remember')
    submit = SubmitField(label='Log In')

    # radio = RadioField(choices=[('value', 'Male'), ('value', 'Female')], default='Male')
