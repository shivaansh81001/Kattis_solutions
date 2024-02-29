'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -NONE

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
'''
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