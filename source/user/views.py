""" The User App views """
from os import abort
from datetime import datetime

from flask import render_template, url_for, redirect, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from source import db, login_manager
from source.user.forms import RegistrationForm, LoginForm, EmailForm, PasswordForm
from source.user.forms import  UpdateAccountForm
from source.user.models import User
from source.utils import generate_confirmation_token, confirm_token
from source.email import send_email

from . import auth_blueprint


@login_manager.user_loader
def load_user(user_id):
    """ User loader """
    return User.query.get(int(user_id))


@auth_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    """ Registration Page Logic """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(lastname=form.lastname.data,firstname=form.firstname.data,
                dob=form.dob.data, address=form.address.data, email=form.email.data,
                password=form.password.data, confirmed=False)
        db.session.add(user)
        db.session.commit()

        token = generate_confirmation_token(user.email)

        confirm_url = url_for('user.confirm_email', token=token, _external=True)
        html = render_template('user/activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)

        flash('A confirmation email has been sent via email.', 'success')
        return redirect(url_for("main.home"))
    return render_template('user/register.html', title='Register', form=form)


@auth_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    """ Login Page logic """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and form.password.data==user.password:
            if user.confirmed:
                login_user(user, remember=form.remember.data)
                next_page = request.args.get("next")
                flash('Login Successful!', 'success')
                return redirect(next_page) if next_page else redirect(url_for('main.home'))

            flash('Please confirmed your account by clicking link send on your mail', 'danger')
            return render_template('login.html', title='Login', form=form)
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('user/login.html', title='Login', form=form)

@auth_blueprint.route("/logout")
def logout():
    """ Logout User Routes"""
    logout_user()
    flash('Logout Successful', 'success')
    return redirect(url_for('user.login'))

@auth_blueprint.route('/confirm/<token>')
def confirm_email(token):
    """ Conformation Registration using email link"""
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('main.home'))

@auth_blueprint.route('/reset', methods=["GET", "POST"])
def reset():
    """ Forgot Password Routes"""
    form = EmailForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first_or_404()

        subject = "Password reset requested"
        token = generate_confirmation_token(form.email.data)

        recover_url = url_for(
            'reset_with_token',
            token=token,
            _external=True)

        html = render_template(
            'user/recover.html',
            recover_url=recover_url)

        # Let's assume that send_email was defined in myapp/util.py
        send_email(user.email, subject, html)

        return redirect(url_for('main.home'))
    return render_template('user/reset.html', form=form)


@auth_blueprint.route('/reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
    """  Token Conformation for Password Reseting """
    try:
        email = confirm_token(token)
    except Exception:
        abort(404)

    form = PasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first_or_404()

        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('reset_with_token.html', form=form, token=token)

@auth_blueprint.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    """ Account Updation """
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.lastname = form.lastname.data
        current_user.firstname = form.firstname.data
        current_user.email = form.email.data
        current_user.dob = form.dob.data
        current_user.gender =  form.gender.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('user.account'))
    if request.method == 'GET':
        form.lastname.data = current_user.lastname
        form.firstname.data = current_user.firstname
        form.email.data = current_user.email
        form.dob.data = current_user.dob
        form.gender.data = current_user.gender.name
        # print(form.gender)
    return render_template('user/account.html', title='Account',
                           form=form)
