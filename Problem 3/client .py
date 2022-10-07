import socket

Host = input("Enter Ip: ")
host = Host #"127.0.0.1"
print(host)
Port = int(input("Enter Port: "))
Port = Port #5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, Port))
    while True:
        sent = input("Client ").encode()
        s.sendall(sent)
        data = s.recv(1024)
        print("Server:",data.decode())

