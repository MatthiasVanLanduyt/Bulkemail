# Import Python Packages
import smtplib
import csv
import getpass
from email.message import EmailMessage

def connect_gmail(email, password):
    

    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.ehlo()
    smtp_object.starttls()
    smtp_object.login(email, password)
    return smtp_object 

# def process_file(inputfile):
    
    

def script(inputfile):

    while True:
        email_server = input('Are you using gmail? Say yes to proceed (we dont support other providers at this stage)')
        if email_server[0] in ('Y', 'y'):
            break
        print("Told you we don't support that!")
    
    sender_email = getpass.getpass('Email from which emails will be send: ')
    sender_password = getpass.getpass('Password: ')
    server = connect_gmail(sender_email, sender_password)
    server.set_debuglevel(1)

    with open(inputfile, mode='r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile, delimiter=';')
        data_lines = list(csv_data)
        for row in data_lines[1:]:
            try:
                
                fullname, recipient_email, subject, body, cc_recipients = row
                # msg = 'Subject: ' + subject + '\n' + body


                # print(f'New row: \nFrom:{sender_email}\nTo:{recipient_email}\nMessage:{msg}')
                # server.sendmail(sender_email, recipient_email, msg)

                msg = EmailMessage()
                msg.set_content(body)
                msg['Subject'] = subject
                msg['From'] = sender_email
                msg['To'] = fullname + ' <' + recipient_email + '>'
                msg['Cc'] = cc_recipients

                # Send the message via our own SMTP server.
                server.send_message(msg)

            except:
                print('Could not send email.')
    server.quit()

# mail_message = '''\
# From: %s
# To: %s
# Subject: %s
# %s
# ''' % (mail_from, mail_to, mail_subject, mail_message_body)# Sent Email
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.login(gmail_user, gmail_password)



script('inputfile.csv')