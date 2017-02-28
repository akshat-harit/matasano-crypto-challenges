#!/usr/bin/env python
'''Decrypt AES-128-ECB text, given the key'''

from base64 import b64decode
from Crypto.Cipher import AES

def decrypt_aes_ecb(key, inp):
    obj = AES.new(key, AES.MODE_ECB)
    text = obj.decrypt(inp)
    return text

def test():
    with open("7.txt") as input_file:
        cipher = input_file.read()
        key = "YELLOW SUBMARINE"
        cipher = b64decode(cipher)
        text = decrypt_aes_ecb(key, cipher)
        print(text)

if __name__ == "__main__":
    test()
