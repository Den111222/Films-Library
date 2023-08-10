from celery import shared_task
from django.core.mail import send_mail

from core.celery import app


# @app.task
@shared_task
def send_spam_email(user_email):
    send_mail(subject='Subject', message='some text',
              from_email='t1937678@gmail.com',
              # recipient_list=['t1937678@gmail.com',],
              recipient_list=[f'{user_email}',],
              )

# def send_spam_email(user_email):
#     print(f"Hello {user_email}")
