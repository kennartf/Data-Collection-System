from flask import abort
from datetime import datetime
from flask_admin import Admin
from sqlalchemy.sql import func
from email.policy import default
from graphene import lazy_import
from E_data_system import db, app
from E_data_system import login_manager
from flask_admin.contrib.sqla import ModelView
from flask_security import UserMixin, RoleMixin
from flask_login import UserMixin, current_user
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey
# from itsdangerous import TimedJSONWEBSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return AdminSession.query.get(int(user_id))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    branch_id = db.Column(db.String(length=100), nullable=False, unique=True)
    username= db.Column(db.String(length=100), nullable=False, unique=True)
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    password = db.Column(db.String(length=100), nullable=False, unique=True)
    image_file = db.Column(db.String(100), nullable=False, default='default.jpeg')
    date_created = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    crm_assembly = db.relationship('CRMAssembly', backref='author', lazy=True, passive_deletes=True)
    youth_registration = db.relationship('Youth_Registration', backref='author', lazy=True, passive_deletes=True)
   
    
    def __repr__(self):
        return f"('{self.branch_id}', '{self.username}')"



class CRMAssembly(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name_of_zone = db.Column(db.String(length=100), nullable=False, unique=True)
    name_of_assembly = db.Column(db.String(length=100), nullable=False, unique=True)
    head_teacher = db.Column(db.String(length=100), nullable=False, unique=True)
    total_no_of_children = db.Column(db.String(length=100), nullable=False, unique=True)
    no_of_children_male = db.Column(db.String(length=50), nullable=False, unique=True)
    no_of_children_female = db.Column(db.String(length=50), nullable=False, unique=True)
    total_no_of_Teachers = db.Column(db.String(length=50), nullable=False, unique=True)
    no_of_teachers_male = db.Column(db.String(length=50), nullable=False, unique=True)
    no_of_teachers_female = db.Column(db.String(length=50), nullable=False, unique=True)
    no_of_souls = db.Column(db.String(length=50), nullable=False, unique=True)
    baptised = db.Column(db.String(length=50), nullable=False, unique=True)
    offering = db.Column(db.String(length=50), nullable=False, unique=True)
    user = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    # date_created = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    
    def __repr__(self):
        return f"('{self.name_of_zone}', '{self.name_of_assembly}')"


class Youth_Registration(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name_of_member = db.Column(db.String(length=100), nullable=False, unique=True)
    gender = db.Column(db.String(length=100), nullable=False, unique=True)
    position1 = db.Column(db.String(length=100), nullable=False, unique=True)
    position2 = db.Column(db.String(length=50), nullable=False, unique=True)
    position3 = db.Column(db.String(length=50), nullable=False, unique=True)
    position4 = db.Column(db.String(length=50), nullable=False, unique=True)
    position5 = db.Column(db.String(length=50), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    town = db.Column(db.String(length=50), nullable=False, unique=True)
    nationality = db.Column(db.String(length=50), nullable=False, unique=True)
    Language = db.Column(db.String(length=50), nullable=False, unique=True)
    contact = db.Column(db.String(length=50), nullable=False, unique=True)
    level_of_education = db.Column(db.String(length=50), nullable=False, unique=True)
    user = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    # date_created = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    
    def __repr__(self):
        return f"('{self.name_of_member}', '{self.gender}', '{self.national_level}')"




class AdminSession(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    branch_id = db.Column(db.String(length=100), nullable=False, unique=True)
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    password = db.Column(db.String(length=100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f"AdminSession('{self.email}')"



admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')


class Controller(ModelView):
    def is_accessible(self):
        if current_user.is_active and current_user.is_active:
            return current_user.is_active
        else:
            return abort(404)

admin.add_view(Controller(User, db.session))
admin.add_view(Controller(CRMAssembly, db.session))
admin.add_view(Controller(Youth_Registration, db.session))
admin.add_view(Controller(AdminSession, db.session))
