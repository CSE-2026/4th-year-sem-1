import cv2
import numpy as np

def embed_msb(img_path, msg):
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Image file '{img_path}' not found")
    
    msg_bin = ''.join(format(ord(char), '08b') for char in msg)
    img_flat = img.flatten()
    
    if len(msg_bin) > len(img_flat):
        raise ValueError("Message is too long to be embedded in the image.")

    msg_len_bin = format(len(msg_bin), '032b')
    msg_bin = msg_len_bin + msg_bin
    
    idx = 0
    for bit in msg_bin:
        img_flat[idx] &= 0b00001111  # Clear the MSB part
        img_flat[idx] |= (int(bit) << 7)  # Set the MSB to the message bit
        idx += 1
    
    img_embedded = img_flat.reshape(img.shape)
    output_path = img_path.split('.')[0] + "_msb_embedded.png"
    cv2.imwrite(output_path, img_embedded)
    print(f"Message embedded successfully in '{output_path}'")

def extract_msb(img_path):
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Image file '{img_path}' not found ")
    
    img_flat = img.flatten()
    
    msg_len_bin = ''.join(str((img_flat[i] & 0b10000000) >> 7) for i in range(32))
    msg_len = int(msg_len_bin, 2)
    
    msg_bin = ''.join(str((img_flat[i] & 0b10000000) >> 7) for i in range(32, 32 + msg_len))
    msg = ''.join(chr(int(msg_bin[i:i+8], 2)) for i in range(0, len(msg_bin), 8))
    
    return msg

if __name__ == '__main__':
    embed_msb('./assets/bunaken.jpg', 'Hey Nithin')
    extracted_msg = extract_msb('_msb_embedded.png')
    print(f"Extracted Message: {extracted_msg}")