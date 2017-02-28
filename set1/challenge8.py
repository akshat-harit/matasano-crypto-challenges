#!/usr/bin/env python
'''Find the text encrypted in AES_ECB'''
from operator import itemgetter

def similarity(inp):
    ''' Higher similarity will imply ECB mode'''
    count = 0
    chunk_size = 32 # 32 hex will be 16 bytes
    for i in range(0, len(inp), chunk_size):
        char = inp[i:i+chunk_size]
        for j in range(0, len(inp), chunk_size):
            if inp[j:j+chunk_size] == char:
                count += 1
    return count

def test():
    with open("8.txt") as input_file:
        out = []
        for line in input_file:
            out.append((line, similarity(line)))
        out.sort(key=itemgetter(1), reverse=True)
        print("Probable ciphertext :", out[0][0])

if __name__ == "__main__":
    test()
