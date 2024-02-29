
def calculate(n,p):
    max_val=2**n
    for i in range(n,-1,-1):
        curr=2**(i) 
        P = curr/max_val
        #print(i,P,curr)
        if P<p:
            P=p
            curr=0
        elif P>=p:
            curr*=(P-p)
        max_val*=(0.5-(P**2)/2)
        #print(max_val)
        max_val=(max_val+curr)/(1-p)
    return max_val

def main():
    while True:
        n,p=map(float,input().split())
        #print(n,p)
        if n==0 and p==0:
            break
        ans=calculate(int(n),p)
        print(f'{ans:.3f}')
main()
        