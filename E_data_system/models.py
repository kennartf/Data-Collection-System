from datetime import datetime
from enum import unique
from sqlalchemy.sql import func
from flask_admin import Admin
from flask_login import UserMixin
from E_data_system import db, app
from E_data_system import login_manager
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey
from itsdangerous import TimedJSONWEBSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
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

    def __repr__(self):
        return f"('{self.name_of_zone}', '{self.name_of_assembly}')"