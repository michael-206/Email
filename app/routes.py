from app import app, db
from flask import render_template, redirect, flash
from flask_login import current_user, login_required, login_user, logout_user
from app.forms import LoginForm, RegisterForm, SendForm
from app.models import User, Email

@app.route('/index')
@app.route('/')
@login_required
def index():
    emails = Email.query.filter_by(toid=current_user.id)
    return render_template('index.html', title='Home', emails=emails)

@app.route('/login', methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect('index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user)
        flash('Login Successful')
        return redirect("/index")
    return render_template('login.html', form=form, title='Login')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)
