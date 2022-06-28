from email.policy import default
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ecommerceapp.model import User

UserType = [('customer','Customer'),('admin', 'Admin'),('shopuser','ShopUser')]
Gender   = [('NA','Not Mentioned'), ('male', 'Male'), ('female', 'Female')]

class RegistrationForm(FlaskForm):
    firstname        = StringField('First Name',validators=[DataRequired(), Length(min=2, max=20)])
    lastname         = StringField('Last Name',validators=[DataRequired(), Length(min=2, max=20)])
    email            = StringField('Email',validators=[DataRequired(), Email()])
    dob              = DateField('DOB', validators=[DataRequired()])
    address          = StringField('Address',validators=[DataRequired()])
    password         = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    usertype         = SelectField('User Type', choices=UserType)
    gender           = SelectField('Gender', choices=Gender)
    submit           = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please choose a different one")


class LoginForm(FlaskForm):
    email    = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit   = SubmitField('Sign in')

class EmailForm(FlaskForm):
    email   = StringField('Email', validators=[DataRequired(), Email()])
    submit  = SubmitField('Submit Email')

class PasswordForm(FlaskForm):
    password         = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit           = SubmitField('Submit Password')

class UpdateAccountForm(FlaskForm):
    firstname = StringField('First Name',validators=[DataRequired(), Length(min=2, max=20)])
    lastname  = StringField('Last Name',validators=[DataRequired(), Length(min=2, max=20)])
    email     = StringField('Email',validators=[DataRequired(), Email()])
    dob       = DateField('DOB', validators=[DataRequired()])
    gender    = SelectField('Gender', choices=Gender)
    submit    = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')