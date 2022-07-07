""" User Database Models"""
from email.policy import default
import enum
from xml.etree.ElementTree import Comment

from flask_login import UserMixin
from source import db


class UserType(enum.Enum):
    """User type enum """
    ADMIN    = "Admin"
    SHOPUSER = "ShopUser"
    CUSTOMER = "Customer"


class Gender(enum.Enum):
    """User Gender Enum """
    NA     = "Not mentioned"
    MALE   = "Male"
    FEMALE = "Female"

class User(db.Model, UserMixin):
    """ User Database Table """
    id              = db.Column(db.Integer, primary_key=True)
    firstname       = db.Column(db.String(20), unique=False, nullable=False)
    lastname        = db.Column(db.String(20), unique=False, nullable=False)
    dob             = db.Column(db.DateTime)
    address         = db.Column(db.String(200), nullable=True)
    email           = db.Column(db.String(120), unique=True, nullable=False)
    password        = db.Column(db.String(120), unique=False, nullable=False)
    usertype        = db.Column(db.Enum(UserType), default=UserType.CUSTOMER, nullable=False)
    gender          = db.Column(db.Enum(Gender), default=Gender.NA, nullable=False)
    confirmed       = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on    = db.Column(db.DateTime, nullable=True)
    approval        = db.Column(db.Boolean, nullable=False, default=False)
    comment         = db.Column(db.String(200), nullable=True)
    action          = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return self.firstname

    def is_admin(self):
        if self.usertype.name == "ADMIN":
            return True
        else:
            return False
    
    def is_shop(self):
        if self.usertype.name == "SHOPUSER":
            return True
        else:
            return False