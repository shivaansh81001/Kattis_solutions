'''
 

  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/is_prime.py

'''

def is_prime(n):
    """returns True if n is prime else False"""
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True
    
def smallest_prime(n):
    n*=2
    n+=1
    #print(n)
    while not is_prime(n):
        #print(n)
        n=n+2
    return n
    
def main():
    
    while(1):
        n=int(input())
        if n==0:
            break
        
        #print(is_prime(7))
        #print(is_prime(6))
        if is_prime(n)==True:
            ans=smallest_prime(n)
            print(ans)
        else:
            ans=smallest_prime(n)
            print(ans,f'({n} is not prime)')
    
main()