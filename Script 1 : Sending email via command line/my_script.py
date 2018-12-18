import argparse
import smtplib
import docx
from os import environ
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_address = environ.get('my_email')
password = environ.get('my_password')

parser = argparse.ArgumentParser()

parser.add_argument("email_id", help="Email ID")
parser.add_argument("subject", help="Subject", type=str)
parser.add_argument("file_path", help="File Path")
args = parser.parse_args()

emailid = args.email_id
sub = args.subject
file_path = args.file_path

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

    msg = MIMEMultipart()

    msg['From'] = my_address
    msg['To'] = emailid
    msg['Subject'] = sub

    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg
    s.quit()


if __name__ == '__main__':
    main()




