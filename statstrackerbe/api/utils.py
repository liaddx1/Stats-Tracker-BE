from django.core.mail import send_mail
from django.conf import settings


def send_welcome_email(to_email):
    subject = "Welcome to My Site"
    message = "Thank you for signing up for our site."
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [to_email]

    send_mail(subject, message, email_from, recipient_list)


def send_which_user_filled_questionnaire(username):
    subject = f"המשתמש {username} מילא את השאלון"
    message = f"{username} המשתמש\nמילא את השאלון וניתן לראות את המידע שלו בפלטפורמה"
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = ["NLFitnessTracker@gmail.com"]

    send_mail(subject, message, email_from, recipient_list)
