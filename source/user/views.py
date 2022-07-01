""" The User App views """
from os import abort
from datetime import datetime

from flask.views import View
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


class Register(View):
    """ Registration Page Logic """
    methods=['GET', 'POST']
    def dispatch_request(self):
        if current_user.is_authenticated:
            return redirect(url_for('main.home'))
        form = RegistrationForm()
        if form.validate_on_submit():
            # print(form.usertype.data)
            if form.usertype.data == "shopuser":
                user = User(lastname=form.lastname.data,firstname=form.firstname.data,
                    dob=form.dob.data, address=form.address.data, email=form.email.data,
                    password=form.password.data, confirmed=False)
                # admin = User.query.filter_by(usertype="ADMIN")
                # print(admin.email)
            else:               
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


class Login(View):
    methods=['GET', 'POST']
    def dispatch_request(self):
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


class Logout(View):
    def dispatch_request(self):
        """ Logout User Routes"""
        logout_user()
        flash('Logout Successful', 'success')
        return redirect(url_for('user.login'))    


class Confirm_email(View):
    """ Conformation Registration using email link"""
    def __init__(self, token):
        self.token = token
    
    def dispatch_request(self):
        try:
            email = confirm_token(self.token)
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


class Reset(View):
    """ Forgot Password Routes"""
    methods=["GET", "POST"]
    
    def dispatch_request(self):
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


class ResetWithToken(View):
    """  Token Conformation for Password Reseting """
    def __init__(self, token):
        self.token = token
    def dispatch_request(self):
        try:
            email = confirm_token(self.token)
        except Exception:
            abort(404)

        form = PasswordForm()

        if form.validate_on_submit():
            user = User.query.filter_by(email=email).first_or_404()

            user.password = form.password.data
            db.session.add(user)
            db.session.commit()
            
            return redirect(url_for('login'))
        return render_template('reset_with_token.html', form=form, token=self.token)


class Account(View):
    methods=['GET', 'POST']
    """ Account Updation """
    @login_required
    def dispatch_request(self):
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

auth_blueprint.add_url_rule('/register', view_func=Register.as_view(name='register'))

auth_blueprint.add_url_rule('/login', view_func=Login.as_view(name='login'))
auth_blueprint.add_url_rule('/logout', view_func=Logout.as_view(name='logout'))
auth_blueprint.add_url_rule('/confirm/<token>', view_func=Confirm_email.as_view(name='confirm_email',))
auth_blueprint.add_url_rule('/reset', view_func=Reset.as_view(name='reset'))
auth_blueprint.add_url_rule('/reset_with_token', view_func=ResetWithToken.as_view(name='reset_with_token'))
auth_blueprint.add_url_rule('/account', view_func=Account.as_view(name='account'))