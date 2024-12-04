import socket

HOST, PORT = "3.70.215.53", 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Type any message to be sent to the server:")

    while True:
        msg = input()

        s.sendall(str.encode(msg))
        print(f"Send [\"{msg}\"] to server!")

        data = s.recv(1024)
        print(f"Received [\"{data.decode()}\"] from server!")