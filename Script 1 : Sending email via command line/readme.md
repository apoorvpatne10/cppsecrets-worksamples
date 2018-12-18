# Script 1 specs

Python program for sending email via commad line.

We can't put email and password directly in variables for obvious reasons. So use of environment variables is preferred. To achieve this, open terminal and type in the following lines one after another:

```
export my_email="email_id@abc.com"
export my_password="password_sample"
```

These are your account's credentials.

### Access them using the os module

```
from os import environ

my_email = environ.get('my_email')
my_password = environ.get('my_password')
```

### To check the optional and positional arguments, type this out in terminal while inside the current directory:

```
user@user:~/Desktop$ python my_script.py -h 

usage: my_script.py [-h] [--email_id EMAIL_ID] subject file_path

positional arguments:
  subject              Subject
  file_path            File Path

optional arguments:
  -h, --help           show this help message and exit
  --email_id EMAIL_ID  Email ID

```

It's clear that positional arguments are mandatory. Optional arguments aren't.
Subject indicates the subject body of an email. File path indicates the path to a .docx file which contains the message to be sent by you.

### To send an email to a particular user, type this in terminal

```
user@user:~/Desktop$ python my_script.py --email_id "friend_mail@gmail.com" "The subject body" "message.docx"
```

This will send the message to the user with specified email id.

### To send an email to multiple people, type this in terminal

```
user@user:~/Desktop$ python my_script.py "The subject body" "message.docx"
```

This will send the message to all the email ids specified in the contacts.txt file.
