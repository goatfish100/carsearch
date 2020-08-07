import os
import smtplib
def send_email( recipient, subject, body):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText


    me = os.getenv('GMAILUSER')
    password = os.getenv('GMAILPASSWORD')

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = recipient

    TO = recipient if type(recipient) is list else [recipient]
    # Record the MIME types of both parts - text/plain and text/html.
    text = "hello world"
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(body, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    # msg.attach(part1)
    msg.attach(part1)
    msg.attach(part2)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(me, password)


    server.sendmail(me, recipient, msg.as_string())
    server.quit()
    print('successfully sent the mail')
