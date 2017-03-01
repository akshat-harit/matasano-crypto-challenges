#!/usr/bin/env python3
''' PKCS#7 padding function'''

def padding_pkcs7(msg, block_size):
    msg_len = len(msg)
    if msg_len == 0:
        return block_size * b'\x04'
    else:
        padding_size = (block_size -(msg_len%block_size))%block_size
        return msg+padding_size*b'\x04'

def test():
    assert padding_pkcs7(b'YELLOW SUBMARINE', 20) == b'YELLOW SUBMARINE\x04\x04\x04\x04'
    assert padding_pkcs7(b'YELLOW SUBMARINE', 3) == b'YELLOW SUBMARINE\x04\x04'
    assert padding_pkcs7(b'', 2) == b'\x04\x04'
    assert padding_pkcs7(b'YELLOW SUBMARINE', 16) == b'YELLOW SUBMARINE'

if __name__ == "__main__":
    test()
