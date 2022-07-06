""" Form module for application"""
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import DateField, SelectField, RadioField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired

from source.user.models import User
from source.user.utils import Constant


class RegistrationForm(FlaskForm):
    """ Form for user Registration """
    firstname        = StringField('First Name',validators=[DataRequired(), Length(min=2, max=20)])
    lastname         = StringField('Last Name',validators=[DataRequired(), Length(min=2, max=20)])
    email            = StringField('Email',validators=[DataRequired(), Email()])
    dob              = DateField('DOB', validators=[DataRequired()])
    address          = StringField('Address',validators=[DataRequired()])
    password         = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=
                                        [DataRequired(),EqualTo('password')])
    usertype         = SelectField('User Type', choices=Constant.UserType)
    gender           = SelectField('Gender', choices=Constant.Gender)
    submit           = SubmitField('Sign Up')

    def validate_email(self, email):
        """ Email validator """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please choose a different one")


class LoginForm(FlaskForm):
    """ Login form """
    email    = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit   = SubmitField('Sign in')


class EmailForm(FlaskForm):
    """ Form for email to send reset link on that email """
    email   = StringField('Email', validators=[DataRequired(), Email()])
    submit  = SubmitField('Submit Email')


class PasswordForm(FlaskForm):
    """ Form for Password submission on reset link """
    password         = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),
                                EqualTo('password')])
    submit           = SubmitField('Submit Password')


class UpdateAccountForm(FlaskForm):
    """ For updating the user account """
    firstname = StringField('First Name',validators=[DataRequired(), Length(min=2, max=20)])
    lastname  = StringField('Last Name',validators=[DataRequired(), Length(min=2, max=20)])
    email     = StringField('Email',validators=[DataRequired(), Email()])
    dob       = DateField('DOB', validators=[DataRequired()])
    gender    = SelectField('Gender', choices=Constant.Gender)
    submit    = SubmitField('Update')

    def validate_email(self, email):
        """ User email validating """
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
            

class RequestForm(FlaskForm):
    """ Form for admin to approve or reject request """
    request_status = RadioField('Request', choices=[(0,'Reject'), (1,'Accept')],
                                 coerce=int, validators=[InputRequired()])
    reason = StringField('Reason')
    submit         = SubmitField('Submit') 