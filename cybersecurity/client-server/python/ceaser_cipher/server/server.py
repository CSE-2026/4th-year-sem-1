import socket

def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

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
            text, shift = data.split('|')
            shift = int(shift)
            processed_text = caesar_cipher(text, shift)
            client_socket.send(processed_text.encode('utf-8'))
        
        client_socket.close()

if __name__ == "__main__":
    start_server()
