#!/usr/bin/env python
''' Code for breaking repeated XOR key cipher'''


def hamming_distance_str(str1, str2):
    hamming_distance = 0
    for char1, char2 in zip(str1, str2):
        xor = ord(char1) ^ ord(char2)
        hamming_distance += bin(xor).count('1')
    return hamming_distance


def test():
    assert hamming_distance_str("this is a test", "wokka wokka!!!") == 37

if __name__ == "__main__":
    test()
