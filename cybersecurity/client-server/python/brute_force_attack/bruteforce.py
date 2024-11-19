from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import base64
import string
import itertools

def des_decrypt(encrypted_text, key):
    encrypted_data = base64.b64decode(encrypted_text)
    iv = encrypted_data[:DES.block_size]
    encrypted_text = encrypted_data[DES.block_size:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text), DES.block_size)
    return decrypted_text.decode('utf-8', errors='ignore')

def brute_force_decrypt(encrypted_text):
    characters = string.ascii_letters + string.digits + string.punctuation
    possible_keys = itertools.product(characters, repeat=8)  # 8 characters key (56 bits)
    
    for key in possible_keys:
        key_str = ''.join(key).encode('utf-8')
        try:
            decrypted_text = des_decrypt(encrypted_text, key_str)
            # Check if decryption is successful (for example, check for specific plaintext format)
            if 'expected_plaintext' in decrypted_text:
                print(f"Found key: {key_str.decode('utf-8')}")
                print(f"Decrypted text: {decrypted_text}")
                return key_str
        except Exception as e:
            continue

    print("Brute-force attack failed.")
    return None

if __name__ == "__main__":
    # Example encrypted text (base64 encoded)
    encrypted_text = b'encrypted_text_here'  # Replace with actual encrypted text
    
    # Perform brute-force attack
    brute_force_decrypt(base64.b64encode(encrypted_text))
