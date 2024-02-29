'''

  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/phi.py


'''
import sys

def phi(n):
    """returns phi(x) for all x <= n"""
    sieve = [i if i & 1 else i // 2 for i in range(n + 1)]
    for i in range(3, n + 1, 2):
        if sieve[i] == i:
            for j in range(i, n + 1, i):
                sieve[j] = (sieve[j] // i) * (i - 1)

    return sieve


def main():
    sieve=phi(10000)  # Precompute totient values up to 10,000
    cases=int(sys.stdin.readline().strip())
    for i in range(cases):
        inp=list(map(int, sys.stdin.readline().strip().split()))
        sys.stdout.write(str(inp[0])+" "+str(1+sum(sieve[1:int(inp[1])+1]))+"\n")

main()