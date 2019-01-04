# chat-crypt

#### Clone this repository by typing the following command in terminal window:

```
git clone https://github.com/apoorvpatne10/chat-crypt
```

#### Once done, cd into it and run server script:

```
apoorv@apoorv:~/Desktop/chat_server$ python serverx.py 
Server IP:  192.168.43.132
Waiting for connection...
```

Now, it's waiting for the client to connect to it. Port is 42000.

#### Get to the know the command line parameters by running the following command

```
apoorv@apoorv:~/Desktop/chat_server$ python client_a.py -h
usage: client_a.py [-h] host port your_name

positional arguments:
  host        Host IP
  port        Port
  your_name   Name

optional arguments:
  -h, --help  show this help message and exit
```

This is similar for client_b as well.

#### Now execute both the scripts, client_a and client_b in separate tabs. A chat window will pop-up for each client:

```
apoorv@apoorv:~/Desktop/chat_server$ python client_a.py 192.168.43.132 42000 apoorv
```
```
apoorv@apoorv:~/Desktop/chat_server$ python client_b.py 192.168.43.132 42000 john
```

#### The server script running on terminal may look like this:

```
apoorv@apoorv:~/Desktop/chat_server$ python serverx.py  
Server IP:  192.168.43.132
Waiting for connection...
('192.168.43.132', 48456) has connected.
('192.168.43.132', 48458) has connected.
Encrypted conversation: 
```

#### Start the conversation now:

![client-a](https://i.imgur.com/jZUPc45.png)

![client-b](https://i.imgur.com/NwBWq5B.png)

#### Here I've made use of RSA encryption algorithm. Server don't have any access to client side's info.

RSA (cryptosystem) RSA (Rivest–Shamir–Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. In such a cryptosystem, the encryption key is public and it is different from the decryption key which is kept secret (private).

#### Her's how the server side will look like once the clients start interacting

![server-side](https://i.imgur.com/r9JfYCQ.png)

