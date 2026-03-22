import smtplib


def mail(sender_email, sender_password, receiver_email, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg)
        server.close()
        return True
    except (smtplib.SMTPException, smtplib.SMTPAuthenticationError, smtplib.SMTPConnectError) as e:
        print(e)
        return False