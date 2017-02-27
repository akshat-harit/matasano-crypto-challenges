#!/usr/bin/env python
''' Functions for repeating-key XOR'''

def hex_byte(byte):
    out = hex(byte)
    out = out[2:]
    if len(out) == 1:
        out = '0' + out
    return out

def hex_text(inp):
    out = []
    for byte in inp:
        out.append(hex_byte(byte))
    return ''.join(out)

def encrypt(key, inp):
    key_len = len(key)
    out = []

    for i in range(0, len(inp)):
        out.append(ord(inp[i]) ^ ord(key[i%key_len]))
    return hex_text(out)

def test():
    inp = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    out = encrypt(key=key, inp=inp)
    assert out == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

if __name__ == "__main__":
    test()
