from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, current_user, login_user, logout_user
from app import app
from app import db
from app.models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        _username = request.form['username']
        _email = request.form['email']
        _password = request.form['password']
        _password_match = request.form['password-match']

        try:
            existing_user = User.query.filter_by(username=_username).first()
            if existing_user is not None:
                print("Username already taken.")
            elif _password != _password_match:
                print("Passwords did not match.")
            new_user = User(username=_username,
                            email=_email)
            new_user.set_password(_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
        except:
            print('There was an error creating your account.')
        return redirect('/')

    return render_template('auth/reg.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']
        user = User.query.filter_by(username=_username).first()

        if user is None or not user.check_password(_password):
            print("invalid credentials")
            return redirect(url_for('login'))
        login_user(user)
        print("login successful!")
        return redirect(url_for('index'))
    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))