'''

  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/gcd.py


'''
def gcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
    return x
    

def main():
    m,n=map(int,input().split())
    g=gcd(m,n)
    temp=1
    while g>1:
        #print(g)
        m=m//g
        n=n//g
        temp*=g
        g=gcd(m,n)
        
        #print(temp)
    #print(m,n)
    #print(g)
    ans=temp*((m%2)*(n%2))
    print(ans)

main()
    