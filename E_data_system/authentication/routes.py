from django.shortcuts import render
from flask import Blueprint, render_template
from E_data_system import db, bcrypt, mail
from flask import render_template, flash, request, redirect, url_for


authent = Blueprint('authent', __name__)



@authent.route('/signup')
def signup():
    return render_template('signup.html')


@authent.route('/login')
def login():
    return render_template('login.html')