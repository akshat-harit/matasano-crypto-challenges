#!/usr/bin/env python
''' Code for breaking repeated XOR key cipher'''
from operator import itemgetter
from base64 import b64decode
from challenge3 import break_single_byte_xor
from challenge5 import hex_text, encrypt

def base64_to_byte(inp):
    return b64decode(inp)


def hamming_distance_str(str1, str2):
    hamming_distance = 0
    for char1, char2 in zip(str1, str2):
        xor = char1 ^ char2
        hamming_distance += bin(xor).count('1')
    return hamming_distance

def probable_keysize_list(inp, max_size=40):
    out_list = []
    for keysize in range(2,max_size):
        array1 = inp[0:keysize]
        array2 = inp[keysize:2*keysize]
        array3 = inp[2*keysize:3*keysize]
        array4 = inp[3*keysize:4*keysize]
        hd = hamming_distance_str(array1,array2)+hamming_distance_str(array1, array3) + hamming_distance_str(array1, array4)
        hd += hamming_distance_str(array2, array3)+ hamming_distance_str(array2, array4)
        hd += hamming_distance_str(array3, array4)
        out_list.append((keysize, hd/(6*keysize)))
    return sorted(out_list, key=itemgetter(1))


def break_repeating_xor(inp):
    inp = base64_to_byte(inp)
    keys = probable_keysize_list(inp)
    print(keys)
    output_key = []
    for k,_ in keys[0:1]:
        print("KEYSIZE =", k)
        for i in range(k):
            chunk = [inp[i+j] for j in range(0, len(inp)-k, k)]
            output_key.append(break_single_byte_xor(hex_text(chunk))[0])
    return ''.join(output_key)


def test():
    assert hamming_distance_str(b"this is a test", b"wokka wokka!!!") == 37
    with open("6.txt") as input_file:
        inp = input_file.read()
        key = break_repeating_xor(inp)
        hex_encrypt = encrypt(key, b64decode(inp).decode('ascii'))
        out  = []
        for i in range(0, len(hex_encrypt), 2):
            out.append(chr(int(hex_encrypt[i:i+2],16)))
        print(''.join(out))
            

if __name__ == "__main__":
    test()
