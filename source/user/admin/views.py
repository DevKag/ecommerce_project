from flask_login import current_user
from flask import redirect, render_template, request, url_for, flash
from flask.views import View

from source import db
from source.user.models import User
from source.user.forms import RegistrationForm, UpdateAccountForm
from source.user.utils import admin_login_required


class ApprovalRequest(View):
    methods=['GET', 'POST']
    
    @admin_login_required
    def dispatch_request(self):

        shop_user = User.query.filter_by(action=0).all()
        return render_template('user/admin/requests.html', context=shop_user)

class Shop(View):
    methods=['GET', 'POST']

    @admin_login_required
    def dispatch_request(self):
        shop_user = User.query.all()
        if request.method == "POST":
            pass
        return render_template('user/admin/shop.html', context=shop_user)
    
class ShopRegistration(View):
    methods=['GET', 'POST']
    
    @admin_login_required
    def dispatch_request(self):
        form = RegistrationForm()
        if request.method == 'POST':
            user = User(firstname=form.firstname.data, lastname=form.lastname.data,
                            dob=form.dob.data, address=form.address.data, email=form.email.data,
                            password=form.password.data, approval=True, confirmed=True, action=True)
            db.session.add(user)
            db.session.commit()
            return redirect('user.shop')
        return render_template('user/admin/shopregister.html', form=form)

class UpdateShop(View):
    methods=['GET', 'POST']
    def dispatch_request(self):
        user_id = request.args.get('id')
        user = User.query.get(int(user_id))
        form = UpdateAccountForm()
        print(request.method)
        print(form.data)
        print(form.validate_on_submit())
        if form.validate_on_submit():
            print(form)
            user.lastname = form.lastname.data
            user.firstname = form.firstname.data
            user.email = form.email.data
            user.dob = form.dob.data
            user.gender =  form.gender.data
            db.session.commit()
            flash('Your account has been updated!', 'success')
            return redirect(url_for('user.shop'))
            
        if request.method == 'DELETE':
            print(request.method)
            db.session.delete(user)
            db.session.commit()
            flash("Your Shop is Deleted successfully", 'success')
            return redirect(url_for('user.shop'))

        if request.method == 'GET':
            form.lastname.data = user.lastname
            form.firstname.data = user.firstname
            form.email.data = user.email
            form.dob.data = user.dob
            form.gender.data = user.gender.name

        return render_template('user/admin/account.html', title='Update Shop',
                            form=form)