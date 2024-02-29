'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/phi.py

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
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