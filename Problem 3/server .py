import socket
Host = input("Enter Ip: ")
host = Host #"127.0.0.1"
print(host)
Port = int(input("Enter Port: "))
Port = Port #5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,Port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected to ", addr)
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                print("Client: ",data.decode())
                sent = input("Server ").encode()
                conn.sendall(sent)
            except ConnectionResetError as e:
                print("Connection lost....!")
                break
            