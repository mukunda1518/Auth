from django.core.mail.message import EmailMessage


class Util:

    @staticmethod
    def send_mail(data):
        print("Hello" * 10)
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        print(email)
        email.send()

