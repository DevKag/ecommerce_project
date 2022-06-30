""" Module For creating token """
from itsdangerous import URLSafeTimedSerializer
from . import create_app

app = create_app()

def generate_confirmation_token(email):
    """ Generate Token While Sending email"""
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=3600):
    """ Genrate Token at the time of conformation"""
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except Exception as e:
        print(e)
        return False
    return email
    