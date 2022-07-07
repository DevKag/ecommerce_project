""" Constant Variable for user app"""
import functools
from flask import redirect, url_for, flash
from flask_login import current_user


class Constant:
    """ Variable list for UserType and whose Gender"""
    UserType = [('customer','Customer'), ('shopuser','ShopUser')]
    Gender   = [('NA','Not Mentioned'), ('MALE', 'Male'), ('FEMALE', 'Female')]

def admin_login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.get_id():
            if current_user.is_admin():
                return func(*args, **kwargs)
            else:
                flash('Admin user login required.', 'danger')
                return redirect(url_for("user.login"))
        else:
            flash('Admin user login required.', 'danger')
            return redirect(url_for("user.login"))
    return wrapper

