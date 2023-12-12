from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail

def send_email_to_enrollers( subject,message,recipient_list):

    from_email = settings.EMAIL_HOST_USER

    send_mail(subject,message, from_email ,recipient_list)