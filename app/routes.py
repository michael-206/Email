from flask_wtf import form
from app import app, db
from flask import render_template, redirect, flash
from flask_login import current_user, login_required, login_user, logout_user
from app.forms import LoginForm, RegisterForm, SendForm, DocumentEditForm, AnswerQuestionForm, AskQuestionForm
from app.models import User, Email, Questions, Documents
import os

@app.route('/email')
@login_required
def index():
    email = current_user.email
    emails = Email.query.filter_by(to=current_user.email)
    return render_template('emailindex.html', title='Home', emails=emails, email=email)

@app.route('/login', methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect('index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
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
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        login_user(user)
    return render_template('register.html', title='Register', form=form)

@app.route('/send', methods=['GET','POST'])
def send():
    form = SendForm()
    if form.validate_on_submit():
        print(form.body.data)
        newemail = Email(subject=form.subject.data, body=form.body.data, to=form.to.data, fromid=current_user.id, fromemail=current_user.email)
        db.session.add(newemail)
        db.session.commit()
        return redirect('/index')
    return render_template('send.html', form=form)

@app.route('/email/<eid>')
def viewemail(eid):
    email = Email.query.get(eid)
    return render_template('email.html', title='View Email', email=email)
