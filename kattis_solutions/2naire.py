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
        