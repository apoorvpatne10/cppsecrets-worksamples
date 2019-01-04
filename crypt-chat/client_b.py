import socket
import argparse
from threading import Thread
import tkinter
import sys
import time
import RSA

parser = argparse.ArgumentParser()

parser.add_argument("host", help="Host IP")
parser.add_argument("port", help="Port")
parser.add_argument("your_name", help="Name")

args = parser.parse_args()

def receive():

    msg_list.insert(tkinter.END, f"Welcome, {NAME}")
    msg_list.insert(tkinter.END, f"You're now online")

    while True:
        try:
            msg = s.recv(BUFFER_SIZE).decode('utf8')
            msg = RSA.decrypt_string(msg, private_key_2)
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break

def send(event = None):
    msg = my_msg.get()
    my_msg.set("")
    msg = NAME + ": " + msg
    msg_list.insert(tkinter.END, msg)
    msg = RSA.encrypt_string(msg, public_key_1)
    s.send(bytes(msg, 'utf8'))

def on_closing(event = None):
    msg_list.insert(tkinter.END, "going offline...")
    # time.sleep(2)
    top.destroy()
    s.close()
    sys.exit()


top = tkinter.Tk()
top.title('Messenger')

msg_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set('Type your message..')
scrollbar = tkinter.Scrollbar(msg_frame)

msg_list = tkinter.Listbox(msg_frame, height=25, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
msg_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind('<Return>', send)
entry_field.pack()
send_button = tkinter.Button(top, text = "Send", command = send)
send_button.pack()

top.protocol('WM_DELETE_WINDOW', on_closing)


HOST = args.host
PORT = args.port
NAME = args.your_name
BUFFER_SIZE = 1024
ADDRESS = (HOST, int(PORT))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDRESS)

public_key_2, private_key_2 = RSA.key_generator()
msg = str(public_key_2[0]) + "*" + str(public_key_2[1])
s.send(bytes(msg, 'utf8'))
m = s.recv(BUFFER_SIZE).decode('utf8')
public_key_1 = [int(x) for x in m.split('*')]

receive_thread = Thread(target = receive)
receive_thread.start()

tkinter.mainloop()
