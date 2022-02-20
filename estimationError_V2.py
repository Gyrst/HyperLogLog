import random
import math
from typing import List
import numpy as np
import matplotlib.pyplot as plt
from hashSuggested import hash_A
from rhoSuggested import rho


def f(x, m_fit):
    res1 = ((x*0xbc164501) & 0x7fffffff) >> m_fit
    return res1

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

#changed the input generation so that it creates a list of n size. One can specify the seed.
def inputGenerator(n: int, seed: int) -> List[int]:
    list= []
    random.seed(seed)
    for i in range(n):
        l = random.getrandbits(32)
        list.append(l)
    return list

hyp_results = []


def registers(M, x: int, m_fit):
    resF = f(x, m_fit) 
    resHash = hash_A(A, x)
    resRho = rho(resHash)
    if(resRho > M[resF]):
        M[resF] = resRho
    # print(M[resF])

def HyperLogLog(M, m):
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


#Put the whole hyperloglog together here with both the register part and hyperloglog calculation
def HyperLogLog_complete(m:int, input:list, m_fit):
    M = [0]*m
    for val in input:
        registers(M, val, m_fit)
    hyperloglog_res = HyperLogLog(M, m)
    return hyperloglog_res
    

#Made this into a separate method to avoid a messy benchmark method

stdv1 = []
stdv2 = []


#I restructured the benchmark into a single method taking the complete hyperloglog and input generations in a loop
def benchmark(iterations, N, m, m_fit):
    
    stdv1_count = 0
    stdv2_count = 0

    sigma = 1.04/math.sqrt(m)
    stdv1plus = N*(1+sigma)
    stdv1min = N*(1-sigma)
    stdv2plus = N*(1+2*sigma)
    stdv2min = N*(1-2*sigma)
    hyp_result_temp = []


    for i in range(iterations):
        input = inputGenerator(N, i)
        res = HyperLogLog_complete(m, input, m_fit)
        print(res) #if you want each of the iteration results printed
        #added a list of the results from our hyperloglog
        hyp_result_temp.append(res)
        #moved this part outside the method

        if (res <= stdv1plus and res >= stdv1min):
            stdv1_count += 1
        if (res <= stdv2plus and res >= stdv2min):
            stdv2_count += 1

    f1 = stdv1_count / iterations
    f2 = stdv2_count / iterations
    hyp_results.append(hyp_result_temp)

    stdv1.append(f1)
    stdv2.append(f2)

#benchmark(iterations=1000, N=10000, m=256) #iterations being how many times we run the test with the our inputs. I 



m_list = [256, 512, 1024, 2048, 4096]
m_fit_origin = 23
#We run the experriment on 100 iterations with a N = 100,000
for element in m_list :
    benchmark(10, 10000, element, m_fit_origin)
    m_fit_origin -= 1 




def write_latex_tabular(ms: List[int],
                        res1: List[float],
                        res2: List[float],
                        mean: List[float],
                        filename: str):
    with open(filename ,'w') as f:
        f.write(r'\begin{tabular}{rrrr}' + '\n')
        f.write(r'$m$& 1 stdv & 2 stdv & mean estimation')
        f.write(r'\\ \hline' + '\n')
        for i in range(len(ms)):
            fields = [str(ms[i]),
                '{:.6f}'.format(res1[i]),
                '{:.6f}'.format(res2[i]),
                '{:.6f}'.format(mean[i])]
            f.write('&'.join(fields) + r'\\' + '\n')
        f.write(r'\end{tabular}' + '\n')

# write_latex_tabular(m_list, stdv1, stdv2,"estimation_error.tex")


# plt.hist(hyp_results, 25) #you can also add int to specify how many intervals there should be in the histogram.

# plt.show()
