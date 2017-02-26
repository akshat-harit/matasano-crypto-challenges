#!/usr/bin/env python
''' This script is for breaking single byte xor message input in hex.'''

from collections import defaultdict

def char_frequency_table(inp="pg98.txt"):
    table = defaultdict(int)
    total = 0
    try:
        with open(inp) as file:
            for line in file:
                for word in line:
                    for char in word:
                        table[char] += 1
                        total += 1
    except IOError:
        print("Sample frequency file not present ", inp)
        exit(1)

    for char in table:
        table[char] = table[char]/total
    return table

def frequency_table(text):
    table = defaultdict(int)
    total = len(text)
    for char in list(text):
        table[char] += 1
    for char in table:
        table[char] = table[char]/total
    return table

def similarity(freq1, freq2):
    denom1 = denom2 = prod = 0
    for key in set(list(freq1.keys())+list(freq2.keys())):
        prod += freq1[key]*freq2[key]
        denom1 += freq1[key]**2
        denom2 += freq2[key]**2
    return prod/((denom1*denom2)**.5)

def decode(inp, key):
    output = []
    for i in range(0, len(inp), 2):
        byte = inp[i:i+2]
        output.append(chr(int(byte, 16)^ ord(key)))
    return ''.join(output)

def break_single_byte_xor(inp):
    base_freq = char_frequency_table()
    output = {}
    for key in range(128):
        text = decode(inp, chr(key))
        similar = similarity(frequency_table(text), base_freq)
        output[chr(key)] = (similar, text)

    max_similar = output['A'][0]
    output_text = output['A'][1]
    output_key = 'A'
    for key in output:
        similar = output[key][0]
        if similar > max_similar:
            max_similar = output[key][0]
            output_key = key
            output_text = output[key][1]
    return output_key, output_text, max_similar

def test():
    inp = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    key, out, _ = break_single_byte_xor(inp)
    print("Key :", key, "\nOutput :", out)

if __name__ == "__main__":
    test()
