from hashSuggested import hash_A
from rhoSuggested import rho
import matplotlib.pyplot as plt
import numpy as np


distr = dict()
probDistr = dict()
probabilityDistribution = np.zeros(20)
def evalHash():
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

    for i in range(1, 1000000):
        hashX = hash_A(A, i)
        rhoHashX = rho(hashX)
        if (distr.get(rhoHashX) == None):
            distr[rhoHashX] = 1
        else:
            distr[rhoHashX] = distr.get(rhoHashX) + 1
        
evalHash()

for r in distr:
    nrOfX = distr[r]
    probabilityDistribution[r] = nrOfX/1000000

print(probabilityDistribution)

# rhos = list(distr.keys())
# xes = list(distr.values())


# plt.plot(rhos, xes)
# plt.show()

# plt.bar(distr.keys(), distr.values(), color='g')
# plt.xlabel('Rho value of hashes')
# plt.ylabel('Number of x')
# # plt.show()
# plt.savefig('Distribution.pdf')

