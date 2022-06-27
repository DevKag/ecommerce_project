from email.policy import default
import enum

from sqlalchemy import null
from ecommerceapp import db, login_manager
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

class UserType(enum.Enum):
    admin    = "Admin"
    shopuser = "ShopUser"
    customer = "Customer"

class Gender(enum.Enum):
    male   = "Male"
    female = "Female"
    NA     = "Not mentioned"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id        = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    lastname  = db.Column(db.String(20), unique=False, nullable=False)
    dob       = db.Column(db.DateTime)
    address   = db.Column(db.String(200), nullable=False)
    email     = db.Column(db.String(120), unique=True, nullable=False)
    password  = db.Column(db.String(120), unique=False, nullable=False)
    usertype  = db.Column(db.Enum(UserType), default=UserType.customer, nullable=False)
    gender    = db.Column(db.Enum(Gender), default=Gender.NA, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f"Username is {self.username}"