import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))  # Connect to port 5000

    text = input("Enter text: ")
    key = input("Enter 8-byte key: ")
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()

    if mode == 'encrypt':
        client_socket.send(f"{text}|{key}|{mode}".encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print("Received from server (encrypted):", response)
    elif mode == 'decrypt':
        encrypted_text = input("Enter encrypted text: ")
        client_socket.send(f"{encrypted_text}|{key}|{mode}".encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print("Received from server (decrypted):", response)

    client_socket.close()

if __name__ == "__main__":
    start_client()
