# Import Python Packages
import smtplib
import csv
import getpass


def connect_gmail(email, password):
    

    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.ehlo()
    smtp_object.starttls()
    smtp_object.login(email, password)
    return smtp_object 

# def process_file(inputfile):
    
    

def script():

    while True:
        email_server = input('Are you using gmail? Say yes to proceed (we dont support other providers at this stage)')
        if email_server[0] in ('Y', 'y'):
            break
        print('Told you we dont support that!')
    
    sender_email = getpass.getpass('Email from which emails will be send: ')
    sender_password = getpass.getpass('Password: ')
    server = connect_gmail(sender_email, sender_password)

    with open(inputfile, mode='r', encoding='UTF-8') as csvfile:
        bulkreader = csv.reader(csvfile, delimiter=';')
        for row in bulkreader:
            
            fullname, email, subject, body, cc_recipients = row

            from_address = sender_email
            to_address = email
            msg = 'Subject: ' + subject + '\n' + body
            server.sendmail(from_address, to_address, msg)
    
    server.close()

# mail_message = '''\
# From: %s
# To: %s
# Subject: %s
# %s
# ''' % (mail_from, mail_to, mail_subject, mail_message_body)# Sent Email
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.login(gmail_user, gmail_password)



script()