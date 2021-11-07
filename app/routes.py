from app import app
from flask import render_template, redirect, flash
#from flask_login import current_user, login_required, login_user, logout_user

@app.route('/index')
@app.route('/')
def index():
    user = 'Michael'
    flash('hello')
    return render_template('index.html', title='Home', user=user)