#################
# Module with function for sending emails.
#################

import smtplib # send the email
from email.mime.multipart import MIMEMultipart # email body
from email.mime.text import MIMEText # email body
import smtp # personal smtp settings

def sendemail(sbj='No-subject',cnt='Email body not specified.'):
    
    print('Composing Email...')

    # update your email details

    SERVER = smtp.SERVER # smtp server
    PORT = smtp.PORT # port number
    FROM = smtp.FROM # sender's email
    TO = smtp.TO # receiver's email (can be a list)
    PASS = smtp.PASS # sender's email smtp password


    msg = MIMEMultipart()
    msg['Subject'] = sbj
    msg['From'] = FROM
    msg['To'] = TO
    msg.attach(MIMEText(cnt, 'html'))

    print('Initiating Server...')

    server = smtplib.SMTP_SSL(SERVER, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    #server.starttls()
    server.login(FROM, PASS)
    server.sendmail(FROM, TO, msg.as_string())

    print('Email Sent...')

    server.quit()