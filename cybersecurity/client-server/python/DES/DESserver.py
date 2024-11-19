import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def des_encrypt(text, key):
    cipher = DES.new(key, DES.MODE_CBC)
    iv = cipher.iv
    padded_text = pad(text.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return base64.b64encode(iv + encrypted_text).decode('utf-8')

def des_decrypt(encrypted_text, key):
    encrypted_data = base64.b64decode(encrypted_text)
    iv = encrypted_data[:DES.block_size]
    encrypted_text = encrypted_data[DES.block_size:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text), DES.block_size)
    return decrypted_text.decode('utf-8')

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))  # Use port 5000 instead of 12345
    server_socket.listen(1)
    print("Server is listening on port 5000")

    while True:
        client_socket, addr = server_socket.accept()
        print("Client connected from", addr)
        
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            text, key, mode = data.split('|')
            key = key.encode('utf-8')
            if mode == 'encrypt':
                processed_text = des_encrypt(text, key)
            elif mode == 'decrypt':
                processed_text = des_decrypt(text, key)
            print(f"Processed text: {processed_text}")
            client_socket.send(processed_text.encode('utf-8'))
        
        client_socket.close()

if __name__ == "__main__":
    start_server()
