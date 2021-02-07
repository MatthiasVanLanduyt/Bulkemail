#Import csv
import csv

# Import smtplib for the actual sending function
import smtplib
import string

# Import the email modules we'll need
from email.message import EmailMessage

def process_file(inputfile):
    
    with open(inputfile, mode='r', encoding='UTF-8') as csvfile:
        bulkreader = csv.reader(csvfile, delimiter=';')
        for row in bulkreader:
            
            fullname, email, subject, body, cc_recipients = row

            smtp_gmail(fullname, email, subject, body, cc_recipients)

# Open the plain text file whose name is in textfile for reading.
def send_email(fullname, email, subject, body, cc_recipients):

    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = 'matthias.vanlanduyt@gmail.com'
    msg['To'] = email

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

def smtp_gmail(fullname, email, subject, body, cc_recipients):
    username = "matthias.vanlanduyt@gmail.com"
    password = "****"
    smtp_server = "smtp.gmail.com:587"
    email_from = "matthias.vanlanduyt@gmail.com"
    email_to = email
    email_body = 'Test test test'
    # email_body = string.join((
    #     "From: %s" % email_from,
    #     "To: %s" % email_to,
    #     "Subject: This is my subject line!",
    #     "",
    #     "This is my message that can also have a %s" % ('Test'
    #     ),), "\r\n"
    #     )
    
    server = smtplib.SMTP(smtp_server)
    server.starttls()
    server.login(username, password)
    server.sendmail(email_from, email_to, email_body)
    server.quit()

process_file('inputfile.csv')