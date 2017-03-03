from base64 import b64decode
from Crypto.Cipher import AES
from challenge9 import padding_pkcs7

def xor(inp1, inp2):
    out = []
    for b1,b2 in zip(inp1, inp2):
        out.append(bytes([b1^b2]))
    return b''.join(out)


def encrypt_aes_ecb(key, inp):
    obj = AES.new(key, AES.MODE_ECB)
    text = obj.encrypt(inp)
    return text

def decrypt_aes_ecb(key, inp):
    obj = AES.new(key, AES.MODE_ECB)
    text = obj.decrypt(inp)
    return text

def encrypt_aes_cbc(iv, key, inp):
    out = []
    if len(iv) != len(key):
        raise InputError("Length of IV and key should be same")
    block_size = len(iv)
    inp = padding_pkcs7(inp, block_size)
    out.append(encrypt(key, xor(iv, inp[0:block_size])))
    
    for i in range(block_size, len(inp), block_size):
        msg = xor(out[i//block_size-1], inp[i:i+block_size])
        out.append(encrypt(key, msg))
    return out

def decrypt_aes_cbc(iv, key, cipher):
    out = []
    if len(iv)!= len(key):
        raise InputError("Length of IV and key should be same")
    block_size = len(iv)
    print("Total length of cipher =", len(cipher))
    for i in range(len(cipher), block_size, -block_size):
        cipher2 = cipher[i-block_size:i]
        print("Cipher 2 is btw", i-block_size,"and", i)
        cipher1 = cipher[i-2*block_size:i-block_size]
        print("Cipher 1 is btw", i-2*block_size,"and", i-block_size)
        text = xor(cipher1, decrypt_aes_ecb(key, cipher2))
        out = out + [text]
        break
#    cipher2 = cipher[0:block_size]
#    text = xor(iv, decrypt_aes_ecb(key, cipher2))
#    out = out + [text]
    return b''.join(out)

def test():
    with open("10.txt", "rb") as input_file:
        key = b'YELLOW SUBMARINE'
        iv = 16*b'\x00'
        text = input_file.read()
        text = decrypt_aes_cbc(iv, key, text)
        print(text)
if __name__ == "__main__":
    test()

