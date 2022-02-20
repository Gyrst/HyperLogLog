import sys

def rho(x):
    for i in range(1,33):
        if ((x >> (32-i)) & 1) == 1:
            return i
    return None


if __name__ == '__main__':
    for line in sys.stdin:
        print(rho(int(line,16)))