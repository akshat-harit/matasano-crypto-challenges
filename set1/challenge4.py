#!/usrbin/env python
''' Given a file with one line encoded with single character xor, find it, and
    output key and decoded value'''

from challenge3 import break_single_byte_xor

def is_ascii_string(inp):
    try:
        inp.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True

def detect_single_char_xor(inp="4.txt"):
    max_similarity = 0
    max_key = ''
    max_out = ""
    max_inp = ""

    with open(inp) as input_file:
        for line in input_file:
            line = line.rstrip('\n')
            key, out, similarity = break_single_byte_xor(line)
            if is_ascii_string(out) and similarity > max_similarity:
                max_key, max_out, max_similarity, max_inp = key, out, similarity, line
    return max_key, max_out, max_inp, max_similarity

def test():
    print(is_ascii_string("This party is rocking"))
    key, out, inp, _ = detect_single_char_xor()
    print("Key :", key, "Decoded text :", out)
    print("Input :", inp)

if __name__ == "__main__":
    test()
