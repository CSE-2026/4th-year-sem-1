import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    capital_letters = input("Enter capital letters: ")
    client_socket.send(capital_letters.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print("Received from server:", response)

    client_socket.close()

if __name__ == "__main__":
    start_client()
