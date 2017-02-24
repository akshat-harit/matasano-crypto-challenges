
def xor(inp1, inp2):
    if len(inp1) != len(inp2):
        raise ValueError("Length of inputs should be equal")
    out = []
    for i1,i2 in zip(inp1,inp2):
        i1, i2 = int(i1,16), int(i2, 16)
        o = hex(i1^i2)
        out.append(o[2:])

    return ''.join(out)
    
def test():
    inp1 = "686974207468652062756c6c277320657965"
    inp2 = "1c0111001f010100061a024b53535009181c"
    out = xor(inp1, inp2)
    expected = "746865206b696420646f6e277420706c6179"
    assert(out == expected)
    print("Test passed")

if __name__ == "__main__":
    test()
