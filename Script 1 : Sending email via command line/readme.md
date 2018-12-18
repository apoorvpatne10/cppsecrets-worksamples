# Script 1 specs

Python program for sending email via commad line.

We can't put email and password directly in variables for obvious reasons. So use of environment variables is preferred. To achieve this, open terminal and type in the following lines one after another:

```
export my_email="email_id@abc.com"
export my_password="password_sample"
```

Access them using the os module

```
from os import environ

my_email = environ.get('my_email')
my_password = environ.get('my_password')
```

