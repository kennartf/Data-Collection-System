from datetime import datetime
from email.policy import default
from graphene import lazy_import
from sqlalchemy.sql import func
from flask_admin import Admin
from flask_login import UserMixin
from E_data_system import db, app
from E_data_system import login_manager
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey
# from itsdangerous import TimedJSONWEBSignatureSerializer as Serializer


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    branch_id = db.Column(db.String(length=100), nullable=False, unique=True)
    username= db.Column(db.String(length=100), nullable=False, unique=True)
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    password = db.Column(db.String(length=100), nullable=False, unique=True)
    image_file = db.Column(db.String(100), nullable=False, default='default.jpeg')
    date_created = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    crm_assembly = db.relationship('CRM_Assembly', backref='author', lazy=True, passive_deletes=True)
    youth_registration = db.relationship('Youth_Registration', backref='author', lazy=True, passive_deletes=True)
   
    
    def __repr__(self):
        return f"('{self.branch_id}', '{self.username}')"



class CRM_Assembly(db.Model, UserMixin):
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
    date_created = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    
    def __repr__(self):
        return f"('{self.name_of_zone}', '{self.name_of_assembly}')"


class Youth_Registration(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name_of_member = db.Column(db.String(length=100), nullable=False, unique=True)
    gender = db.Column(db.String(length=100), nullable=False, unique=True)
    national_level= db.Column(db.String(length=100), nullable=False, unique=True)
    position1 = db.Column(db.String(length=100), nullable=False, unique=True)
    name_of_region = db.Column(db.String(length=50), nullable=False, unique=True)
    position2 = db.Column(db.String(length=50), nullable=False, unique=True)
    name_of_distric = db.Column(db.String(length=50), nullable=False, unique=True)
    position3 = db.Column(db.String(length=50), nullable=False, unique=True)
    name_of_zone = db.Column(db.String(length=50), nullable=False, unique=True)
    position4 = db.Column(db.String(length=50), nullable=False, unique=True)
    name_of_assembly = db.Column(db.String(length=50), nullable=False, unique=True)
    position5 = db.Column(db.String(length=50), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    town = db.Column(db.String(length=50), nullable=False, unique=True)
    nationality = db.Column(db.String(length=50), nullable=False, unique=True)
    Language = db.Column(db.String(length=50), nullable=False, unique=True)
    contact = db.Column(db.String(length=50), nullable=False, unique=True)
    level_of_education = db.Column(db.String(length=50), nullable=False, unique=True)
    user = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    
    def __repr__(self):
        return f"('{self.name_of_member}', '{self.gender}', '{self.national_level}')"