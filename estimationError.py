import random
import math
from typing import List
import numpy as np
# from hyperLogLogKtob import HyperLogLog
# from registersKtob import registers
from hashSuggested import hash_A
from rhoSuggested import rho

m = 256
N = 500000
sigma = 1.04/math.sqrt(m)
stdv1plus = N*(1+sigma)
stdv1min = N*(1-sigma)
stdv2plus = N*(1+2*sigma)
stdv2min = N*(1-2*sigma)

def f(x):
    res = ((x*0xbc164501) & 0x7fffffff) >> 23
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



def inputGenerator(n: int, seed: int) -> List[int]:
    list= []
    for i in range(0,n):
        random.seed(i+seed)
        l = random.getrandbits(32)
        list.append(l)
    return list

results = {'std1': 0, 'std2': 0}

def HyperLogLog():
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


def benchmark():
    hyperLog = HyperLogLog()
    print(hyperLog)
    if (hyperLog <= stdv1plus and hyperLog >= stdv1min):
        current = results.get('std1')
        current += 1
        results['std1'] = current
    if (hyperLog <= stdv2plus and hyperLog >= stdv2min and (hyperLog > stdv1plus or hyperLog < stdv1min)):
        current = results.get('std2')
        current += 1
        results['std2'] = current


def registers(x: int):
    resF = f(x) 
    resHash = hash_A(A, x)
    resRho = rho(resHash)
    if(resRho > M[resF]):
        M[resF] = resRho
    # print(M[resF])

input = inputGenerator(N, 3)

for i in range(0,10):
    M = [0]*m
    for val in input:
        registers(val)
    benchmark()

print(results)

# def write_latex_tabular(ns: List[int],
#                         res: np.ndarray ,
#                         filename: str):
#     with open(filename ,'w') as f:
#         f.write(r'\begin{tabular }{rrr}' + '\n')
#         f.write(r'$n$& Average & Standard deviation ')
#         f.write(r'\\ \hline' + '\n')
#         for i in range(len(ns)):
#             fields = [str(ns[i]),
#                 '{:.6f}'.format(res[i,0]),
#                 '{:.6f}'.format(res[i,1])]
#             f.write('&'.join(fields) + r'\\' + '\n')
#         f.write(r'\end{tabular}' + '\n')