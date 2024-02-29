'''

  -https://www.geeksforgeeks.org/compute-ncrp-using-fermat-little-theorem/
  -https://www.geeksforgeeks.org/queries-of-ncrp-in-o1-time-complexity/

'''
P = 1000000007

def ncr(n,k,fact,inv_fact):
    if k<0 or k>n:
        return 0
    return (fact[n]*inv_fact[k]*inv_fact[n-k])%P

def power(x,y,p):
    result=1
    x = x%p
    while y>0:
        if y&1:
            result=(result*x)%p
        y>>=1
        x=(x*x) % p
    return result

def mod_inverse(x,p):
    return power(x,p-2,p)



def formula(N, K, vals):
    ans = 0
    memo={}
    
    fact=[1]*(N+1)
    inv_fact=[1]*(N+1)
    for i in range(1, N+1):
        fact[i]=(fact[i-1]*i)%P
    inv_fact[N]=mod_inverse(fact[N],P)
    for i in range(N-1,-1,-1):
        inv_fact[i]=(inv_fact[i+1]*(i+1)) % P
        
    
    for val in vals:
        memo[val]=memo.get(val,0) + 1

    
    sett=list(set(vals))
    sett.reverse()
    count=len(vals)

    for temp in sett:
        if count<3:
            break
        ans+=temp*(ncr(count, K, fact, inv_fact)-ncr(count-memo[temp],K,fact,inv_fact))
        ans %= P
        count-=memo[temp]
    return ans

        
def main():
    N,K=map(int,input().split())
    vals=sorted([eval(x) for x in input().split()])
    ans=formula(N,K,vals)
    print(ans%P)
    
   
main()