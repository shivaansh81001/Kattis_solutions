
import math

def solve(n,m):
    cnt=0
    sq=min(n,int(math.sqrt(m)))
    i=1
    while i<sq+1:
        if m%i!=0:
            pass
        else:
            if m/i<=n:
                cnt+=1
            if i!=m/i and m/i<=n:
                cnt+=1
        i+=1
    return cnt
    
def main():
    n,m=map(int,input().split())
    print(solve(n,m))
    
main()