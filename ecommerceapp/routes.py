from flask import render_template, url_for, make_response, redirect, request, flash
from flask import current_app as app
from datetime import datetime
from ecommerceapp import db
from ecommerceapp.forms import RegistrationForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from ecommerceapp.model import User
from ecommerceapp.token import generate_confirmation_token, confirm_token

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.dob.data)
        user = User(lastname=form.lastname.data,firstname=form.firstname.data, dob=form.dob.data, 
                    address=form.address.data, email=form.email.data, password=form.password.data, 
                    confirmed=False)
        db.session.add(user)
        db.session.commit()
        token = generate_confirmation_token(user.email)
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and form.password.data:
            login_user(user, remember=form.remember.data)
            flash('Login Successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash('Logout Successful', 'success')
    return render_template('logout.html')