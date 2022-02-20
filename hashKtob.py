import fileinput
import numpy as np

matrixData = [0x21ae4036, 0x32435171, 0xac3338cf, 0xea97b40c, 
            0x0e504b22, 0x9ff9a4ef, 0x111d014d, 0x934f3787, 
            0x6cd079bf, 0x69db5c31, 0xdf3c28ed, 0x40daf2ad, 
            0x82a5891c, 0x4659c7b0, 0x73dc0ca8, 0xdad3aca2, 
            0x00c74c7e, 0x9a2521e2, 0xf38eb6aa, 0x64711ab6, 
            0x5823150a, 0xd13a3a9a, 0x30a5aa04, 0x0fb9a1da, 
            0xef785119, 0xc9f0b067, 0x1e7dde42, 0xdda4a7b2,
            0x1a1c2640, 0x297c0633, 0x744edb48, 0x19adce93]

Matrix = np.zeros((32,32))


def getBit(hex: int, position: int):
    return ((hex >> position) & 1)


for i in range(0,32):
    converted = []
    x = matrixData[i]
    for j in range(0,32):
        converted = [getBit(x,j)] + converted  
    Matrix[i] = converted


multi = [31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
# vector for converting the output vector to decimal result
def makeConVector():
    conVector = np.zeros((32,1))
    for i in range(31,-1, -1):
        conVector[i] = 2**(multi[i])
    return conVector


for line in fileinput.input():
    num = int(line.rstrip(), 16)
    x = np.zeros((32,1))
    y=[]
    for i in range(31,-1,-1):
        x[i] = getBit(num, 31-i)
    print(line)
    print(x)
    outputVec = np.dot(Matrix, x)
    mod2 = (outputVec % 2)
    y = np.zeros((32,1))
    for i in range(31,-1,-1):
        y[i] = mod2[31-i]
    transp = y.transpose()
    output = np.dot(transp, makeConVector())[0,0]
    result = format(int(output),'x')
    if len(result) < 8:
        for i in range(8-len(result)):
            result = str(0) + result
    print(result)

