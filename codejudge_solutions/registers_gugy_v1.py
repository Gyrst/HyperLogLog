import sys 

#Given alternative hash

# 20 --> M of 2048
# 21 --> M of 1024
# 22 --> M of 512
# 23 --> M of 256

def f(x):
    return ((x*0xbc164501) & 0x7fffffff) >> 21

#Debugging the indexing function:

# - The right shift ">>" halfes the indexing size.
# - See for yourself below when testing

# for i in range(100):
#     print(f(randint(0,10000000), 23))

def rho(x):
    for i in range(32+1): # as we want 32 inclusive
        #print("i is:",i)
        #print("shift_result:", x >> 32-i)
        if (x >> 32-i & 1):
            return i

def popcount(x):
    c = 0
    while x != 0:
        c += x & 1
        x >>= 1
    return c



def getBit(hex: int, position: int):
    return ((hex >> position) & 1)
    
def hash_A(A, x):
    h = 0
    for i in range(32):
        h |= ((popcount(A[i]&x)&1) << i)
    return h


A_hex = [0x21ae4036,
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

#lines = [0x076d07ce, 0x3626ff0c, 0x82e1268a, 0x9128b79c, 0x30e2346f]

for line in sys.stdin:
    line = int(line, 16)
    index = f(line) #what bin it goes in
    hash_val = hash_A(A_hex, line)
    rho_of_hash = rho(hash_val)
    if M[index] < rho_of_hash:
        M[index] = rho_of_hash



for val in M:
    print(val)