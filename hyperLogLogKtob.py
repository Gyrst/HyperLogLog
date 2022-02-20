from hashSuggested import hash_A
from rhoSuggested import rho
from registersKtob import registers
import math
import sys

def f(x):
    res = ((x*0xbc164501) & 0x7fffffff) >> 21
    return res

A = [0x21ae4036,
    0x32435171,
    0xac3338cf,
    0xea97b40c,
    0x0e504b22,
    0x9ff9a4ef,
    0x111d014d,
    0x934f3787,
    0x6cd079bf,
    0x69db5c31,
    0xdf3c28ed,
    0x40daf2ad,
    0x82a5891c,
    0x4659c7b0,
    0x73dc0ca8,
    0xdad3aca2,
    0x00c74c7e,
    0x9a2521e2,
    0xf38eb6aa,
    0x64711ab6,
    0x5823150a,
    0xd13a3a9a,
    0x30a5aa04,
    0x0fb9a1da,
    0xef785119,
    0xc9f0b067,
    0x1e7dde42,
    0xdda4a7b2,
    0x1a1c2640,
    0x297c0633,
    0x744edb48,
    0x19adce93 ]

M = [0]*1024

def HyperLogLog():
    m = 1024
    alfaM = 0.7213/(1 + 1.079/m)
    sum = 0
    for i in range(0,m):
        sum += math.pow(2, -M[i])
    n = alfaM * math.pow(m, 2) * (math.pow(sum, -1))
    V = 0
    pow2 = math.pow(2,32)
    for x in M:
        if(x==0):
            V += 1
    if (n <= ((5/2)*m)) and V > 0:
        return m*(math.log(m/V))
    if (n > (1/30)*pow2):
        n = -pow2*(math.log(1-(n/pow2)))
    return n

if __name__ == '__main__':
    threshold = int(sys.stdin.readline().strip())
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        input = int(line)
        registers(input)

    hyperLog = HyperLogLog()   

    if(hyperLog < threshold):
        print("below")
    if(hyperLog > threshold):
        print("above")