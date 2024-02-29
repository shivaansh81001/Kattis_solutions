'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  for factorial/ inverse factorial :
  -https://www.geeksforgeeks.org/compute-ncrp-using-fermat-little-theorem/
  -https://www.geeksforgeeks.org/queries-of-ncrp-in-o1-time-complexity/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
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