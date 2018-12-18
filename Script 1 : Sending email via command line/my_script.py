import argparse
import smtplib
import docx
import re
from os import environ
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_address = environ.get('my_email')
password = environ.get('my_password')

parser = argparse.ArgumentParser()

parser.add_argument("--email_id", help="Email ID")
parser.add_argument("subject", help="Subject", type=str)
parser.add_argument("file_path", help="File Path")
args = parser.parse_args()

if args.email_id:
    emailid = args.email_id
sub = args.subject
file_path = args.file_path

def is_valid_email(email):
    my_pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
    pattern = re.compile(my_pattern)

    if re.match(pattern, email):
        return True
    else:
        return False

def get_contacts(filename):
   emails = []

   with open(filename, mode='r', encoding='utf-8') as contacts_file:
       for contact in contacts_file:
           emails.append(contact.split()[0])

   return emails

def main():

    doc_file = docx.Document(file_path)
    paragraphs = doc_file.paragraphs
    message = ''

    for para in paragraphs:
        message += para.text
        message += '\n'

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(my_address, password)

    if args.email_id:

        msg = MIMEMultipart()

        msg['From'] = my_address
        msg['To'] = emailid
        msg['Subject'] = sub

        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg
        s.quit()

        print('Email sent successfully!')
    else:
        print("Sending emails to all contacts provided in the contacts file")
        emails = get_contacts('contacts.txt')

        for email in emails:
            if is_valid_email(email):
                msg = MIMEMultipart()

                msg['From'] = my_address
                msg['To'] = email
                msg['Subject'] = sub

                msg.attach(MIMEText(message, 'plain'))
                s.send_message(msg)
                del msg
                print('Email sent!')
            else:
                print("Invalid email. This will be ignored and message won't be sent.")

        s.quit()


if __name__ == '__main__':
    if args.email_id:
        if is_valid_email(emailid) and type(emailid) == str and type(sub) == str and type(file_path) == str:
            main()
        else:
            print("Invalid email or invalid file paths or subject")
    else:
        if type(sub) == str and type(file_path) == str:
            main()
        else:
            print("Invalid file paths or subject")




