from flask_mail import Mail, Message

mail = Mail()


def send_password_reset_email(user, codes):
    code = str(codes)
    msg = Message(subject='Изменить пароль от OSI.HElP',
                  sender='OSI.HELP',
                  recipients=[user.email],
                  body=f'''Код для изменения пароля {code} ''')
    mail.send(msg)


