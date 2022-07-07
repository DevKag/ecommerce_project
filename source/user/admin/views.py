from flask import render_template
from flask.views import View


from source.user.models import User
from source.user.utils import admin_login_required


class ApprovalRequest(View):
    methods=['GET', 'POST']
    
    @admin_login_required
    def dispatch_request(self):

        shop_user = User.query.filter_by(action=0).all()
        return render_template('user/admin/requests.html', context=shop_user)

class Shop(View):
    methods=['GET', 'POST']

    # @admin_login_required
    def dispatch_request(self):
        shop_user = User.query.filter_by(action=0).all()
        return render_template('user/admin/shop.html', context=shop_user)