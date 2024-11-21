import cv2
import numpy as np

def embed(img_path, msg):
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Image file '{img_path}' not found.")
    
    # Convert message to binary
    msg_bin = ''.join(format(ord(char), '08b') for char in msg)
    img_flat = img.flatten()
    
    if len(msg_bin) > len(img_flat):
        raise ValueError("Message is too long to be embedded in the image.")
    
    # Prepend the message length
    msg_len_bin = format(len(msg_bin), '032b')
    msg_bin = msg_len_bin + msg_bin
    
    # Embed the message in the least significant bits
    idx = 0
    for bit in msg_bin:
        img_flat[idx] &= 0b11111110
        img_flat[idx] |= int(bit)
        idx += 1
    
    img_embedded = img_flat.reshape(img.shape)
    output_path = img_path.split('.')[0] + "_lsb_embedded.png"
    cv2.imwrite(output_path, img_embedded)
    print(f"Message embedded successfully in '{output_path}'")

def extract(img_path):
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Image file '{img_path}' not found or could not be opened.")
    
    img_flat = img.flatten()
    
    # Extract the message length
    msg_len_bin = ''.join(str(img_flat[i] & 1) for i in range(32))
    msg_len = int(msg_len_bin, 2)
    
    # Validate message length
    if msg_len > len(img_flat) - 32:
        raise ValueError("Extracted message length is invalid or corrupted.")
    
    # Extract the message binary
    msg_bin = ''.join(str(img_flat[i] & 1) for i in range(32, 32 + msg_len))
    msg = ''.join(chr(int(msg_bin[i:i+8], 2)) for i in range(0, len(msg_bin), 8))
    
    return msg

if __name__ == '__main__':
    embed('./assets/man.jpeg', 'Hello, World! This document will self-destruct, and all personnel are required to acknowledge their understanding of the contents before proceeding with their assigned tasks.')
    extracted_msg = extract('_lsb_embedded.png')
    print(f"Extracted Message: {extracted_msg}")
