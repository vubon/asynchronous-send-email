from django.core.mail import send_mail


def send_feedback_email(name, email, message):
    send_mail(name, message + " \n " + email, email, ['vubon.roy@gmail.com'], fail_silently=False)
