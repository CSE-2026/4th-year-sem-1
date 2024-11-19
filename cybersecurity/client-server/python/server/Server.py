import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345")

    while True:
        client_socket, addr = server_socket.accept()
        print("Client connected from", addr)
        
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            lowercase_data = data.lower()
            client_socket.send(lowercase_data.encode('utf-8'))
        
        client_socket.close()

if __name__ == "__main__":
    start_server()
