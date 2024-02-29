'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -https://stackoverflow.com/questions/11809502/which-is-better-way-to-calculate-ncr

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
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