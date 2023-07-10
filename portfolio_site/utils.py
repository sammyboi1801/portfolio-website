from django.core.mail import send_mail
from django.conf import settings

def send_email_from_client(email, message):
    subject = "Message by " + str(email)
    message = message
    from_email = settings.EMAIL_HOST_USER
    # print(from_email)
    recipient_list = ["samselvaraj1801@gmail.com"]
    send_mail(subject,message, from_email, recipient_list)

def send_email_to_client(email):
    subject = "Here you go! :)"
    message = "Here's my CV: https://drive.google.com/file/d/1FV_3fG6ouPOQbVN5WfGrpQu7kUVuBvu-/view?usp=sharing"
    from_email = settings.EMAIL_HOST_USER
    # print(from_email)
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
