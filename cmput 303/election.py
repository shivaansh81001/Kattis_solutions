'''


  -https://stackoverflow.com/questions/11809502/which-is-better-way-to-calculate-ncr

'''
def ncr(n, r):
    if r > n - r:
        r = n - r
    ans = 1

    for i in range(1, r + 1):
        ans *= n - r + i
        ans //= i

    return ans

def result(n,v1,v2,w):
    if v2>=(n+1)//2:
        return "RECOUNT!"
    elif v1>n//2:
        return "GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!"
    else:
        temp=0
        m=n-(v1+v2)
        for i in range(n//2+1-v1,m+1):
            temp+=ncr(m,i)/2**m
        if temp>w:
            return "GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!"
        else:
            return "PATIENCE, EVERYONE!"

def main():
    cases=int(input())
    for i in range(cases):
        n,v1,v2,w=map(int,input().split())
        w/=100
        #print(w)
        ans=result(n,v1,v2,w)
        print(ans)
main()