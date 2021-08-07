#!/usr/bin/env python3
from Crypto.Util.number import getPrime
import re
import sys

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

FLAG = open('flag.txt', 'rb').read()

def generate(nbit):
    x = nbit // 16
    e = getPrime(x * 5)
    p = getPrime(x * 7)
    q = getPrime(x * 9)
    return [e, p * q]

def main():
    e, n = generate(224)
    m = int.from_bytes(re.findall(br'^gemastik14{(\w+)}$', FLAG)[0], 'big')
    assert m < n
    c = pow(m, e, n)
    print(f'<< {c}')
    for _ in range(3):
        m = int(input('>> '))
        assert m > 0
        c = pow(m, e, n)
        print(f'<< {c}')

if __name__ == '__main__':
    main()
