import numpy as np
import sys

A_hex = [0x21ae4036, 0x32435171, 0xac3338cf, 0xea97b40c, 0x0e504b22, 0x9ff9a4ef, 0x111d014d, 0x934f3787, 0x6cd079bf, 0x69db5c31, 0xdf3c28ed, 0x40daf2ad, 0x82a5891c, 0x4659c7b0, 0x73dc0ca8, 0xdad3aca2, 0x00c74c7e, 0x9a2521e2, 0xf38eb6aa, 0x64711ab6, 0x5823150a, 0xd13a3a9a, 0x30a5aa04, 0x0fb9a1da, 0xef785119, 0xc9f0b067, 0x1e7dde42, 0xdda4a7b2, 0x1a1c2640, 0x297c0633, 0x744edb48, 0x19adce93]


def getBit(hex: int, position: int):
    return ((hex >> position) & 1)


def get_A(list_of_hex):
    A = np.zeros((32,32))
    for i in reversed(range(32)):
        row = []
        for j in reversed(range(32)):
            row += [getBit(list_of_hex[i], j)]
        A[i] = row
    return A


def hash(x, A):
    x_as_np = np.zeros((32,1))

    for i in reversed(range(32)):
        x_as_np[i] = getBit(int(x,16), 31-i)

    #print(x_as_np)

    matrix_dot = np.dot(A,x_as_np)

    res_bin = matrix_dot % 2

    res_bin = res_bin.T

    bin_str = ""
    for bin in reversed(res_bin[0]):
        bin_str += str(int(bin))

    res_hex_rep = hex(int(bin_str, 2))

    return res_hex_rep[2:].zfill(8)

A = get_A(A_hex)

# test_input =   ['00000001',
#                 '00000002',
#                 '00000003',
#                 '00000004',
#                 '00000005']

# for input in test_input:
#     print(hash(input, A))

for line in sys.stdin:
    print(hash(line, A))