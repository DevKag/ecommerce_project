""" This Module is for Email sending"""
from flask_mail import Message

from . import create_app, mail

app = create_app()


def send_email(to_email, subject, template):
    """ Fuction to send mails"""
    msg = Message(
        subject,
        recipients=[to_email],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)
