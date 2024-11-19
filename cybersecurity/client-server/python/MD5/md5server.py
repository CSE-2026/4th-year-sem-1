import socket
import hashlib

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

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
            hashed_text = md5_hash(data)
            print(f"Received text: {data}, MD5 hash: {hashed_text}")
            client_socket.send(hashed_text.encode('utf-8'))
        
        client_socket.close()

if __name__ == "__main__":
    start_server()
