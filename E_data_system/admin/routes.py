from flask import Blueprint
from flask_mail import Message
from flask import get_flashed_messages
from E_data_system import db, bcrypt, mail
from flask import url_for, flash, request, redirect, render_template, 



admin = Blueprint('admin', __name__)



