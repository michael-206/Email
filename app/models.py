from app import db
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
	    return "<{}:{}>".format(self.id, self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Email(db.Model):
    __tablename__ = 'Email'
    id = db.Column(db.Integer(), primary_key=True)
    subject = db.Column(db.String(50), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    to = db.Column(db.Integer(), nullable=False)
    fromid = db.Column(db.Integer(), nullable=False)
    fromemail = db.Column(db.String(50), nullable=False)
    

    def __repr__(self):
	    return "<{}:{}>".format(self.id, self.body)

class Questions(db.Model):
    __tablename__ = 'Questions'
    id = db.Column(db.Integer(), primary_key=True)
    question = db.Column(db.Text(), nullable=False)
    answer = db.Column(db.Text(), nullable=False)
    

    def __repr__(self):
	    return "<{}:{}>".format(self.id, self.question)

class Documents(db.Model):
    __tablename__ = 'Documents'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    

    def __repr__(self):
	    return "<{}:{}>".format(self.id, self.title)