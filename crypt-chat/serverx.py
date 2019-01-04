import socket
from threading import Thread


client_sock = []
client_addresses = {}
public_key = []

class MyServer:

    def __init__(self, host, port, buff_size, sock):
        self.HOST = host
        self.PORT = port
        self.BUFFER_SIZE = buff_size
        self.ADDRESS = (self.HOST, self.PORT)
        self.s = sock

    def accept_incoming_connections(self):
        conn, addr = self.s.accept()
        client_sock.append(conn)
        print(f"{addr} has connected.")
        public_key.append(conn.recv(self.BUFFER_SIZE))
        client_addresses[conn] = addr


    def handle_client1(self, client_sock, client_addresses):
        client_sock[0].send(public_key[1])

        while True:
            message_a = client_sock[0].recv(self.BUFFER_SIZE)
            client_sock[1].send(message_a)
            print(f"Client A: {message_a.decode('utf8')}")


    def handle_client2(self, client_sock, client_addresses):
        client_sock[1].send(public_key[0])

        while True:
            message_b = client_sock[1].recv(self.BUFFER_SIZE)
            client_sock[0].send(message_b)
            print(f"Client B: {message_b.decode('utf8')}")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())

obj = MyServer(host, 42000, 1024, s)

obj.s.bind(obj.ADDRESS)

obj.s.listen(2)

print("Server IP: ", obj.HOST)
print("Waiting for connection...")

obj.accept_incoming_connections()
obj.accept_incoming_connections()

Thread(target = obj.handle_client1, args = (client_sock, client_addresses)).start()
Thread(target = obj.handle_client2, args = (client_sock, client_addresses)).start()
print('Encrypted conversation: ')

obj.s.close()







