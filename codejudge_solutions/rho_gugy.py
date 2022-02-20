import sys

def rho(x):
    x = int(x,16)
    for i in range(32+1): # as we want 32 inclusive
        print("i is:",i)
        print("shift_result:", x >> 32-i)
        if (x >> 32-i & 1):
            return i

# for line in sys.stdin:
#     print(rho(line))

test_input = '80000000'
test_input32 = '00000001'
test_input31 = '00000002'
binrep = "{:032b}".format(int(test_input, 16))
print(binrep)

print(rho(test_input))

""" - When we shift right shift bits we half the numbers size, and when we shift left we double its size
    - The reason that it never returns i as 0 is the shift made is 0, so no shift basically.
    - When we shift 1 it matches to counting the 1 element in the bit representation of the number (counting from the right to left).
    - This is why we need to take 32-i to ensure we count from left to right.
"""