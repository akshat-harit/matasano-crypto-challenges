def Base64Table():
    table = {}
    for i in xrange(0,26):
        table[i] = chr(ord('A') + i)
    for i in xrange(26,52):
        table[i] = chr(ord('a')+i-26)
    for i in xrange(52,62):
        table[i] = chr(ord('0')+i - 52) 
    table[62] = '+'
    table[63]= '/'
    return table

def hexOctetToBase64(inp):
    Table = Base64Table()
    inp = int(inp, 16)
    digit1 = Table[inp%64]
    digit2 = Table[inp//64]
    return digit2+digit1

def hexToBase64(inp):
    out = []
    temp = ""
    for byte in inp[::-1]:
        temp = byte + temp
        if len(temp) == 3: 
            out.append(hexOctetToBase64(temp))
            temp = ""
    if temp!='':
        out.append(hexOctetToBase64(temp))
    return ''.join(out[::-1])

def test():
    assert(hexOctetToBase64('f6d') == '9t')
    inp = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    out = hexToBase64(inp)
    assert(out == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")
    print("Tests passed")

if __name__ == '__main__':
    test()
