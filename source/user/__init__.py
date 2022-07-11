""" Initilization and Blueprint file for User App"""
from flask import Blueprint

auth_blueprint = Blueprint('user', __name__, template_folder='templates')

from . import views

from .admin.views import ApprovalRequest, Shop, ShopRegistration, UpdateShop

auth_blueprint.add_url_rule('/approval_request',view_func=ApprovalRequest.as_view(name='approval_requests'))
auth_blueprint.add_url_rule('/shop', view_func=Shop.as_view(name='shop'))
auth_blueprint.add_url_rule('/shopregistation', view_func=ShopRegistration.as_view(name='shop_registration'))
auth_blueprint.add_url_rule('/shopupdate', view_func=UpdateShop.as_view(name='shop_update'))
