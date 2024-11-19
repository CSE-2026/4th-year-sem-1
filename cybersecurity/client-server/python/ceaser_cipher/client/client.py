import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))
    client_socket.send(f"{text}|{shift}".encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print("Received from server (encrypted):", response)

    # Optionally, decrypt the response
    decrypt = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
    if decrypt == 'yes':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 12345))
        client_socket.send(f"{response}|{-shift}".encode('utf-8'))
        decrypted_response = client_socket.recv(1024).decode('utf-8')
        print("Received from server (decrypted):", decrypted_response)

    client_socket.close()

if __name__ == "__main__":
    start_client()
