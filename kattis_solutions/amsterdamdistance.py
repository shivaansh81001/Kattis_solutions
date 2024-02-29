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

def calc(m,n,r,x1,y1,x2,y2):
    pi=3.14159265358979
    ans=0
    if y1<y2:
        if abs(x1-x2)*(pi/m)/2<=1.0:
            ans+=(abs(x1-x2)*(pi/m)*y1*r)/n
        else:
            ans+=(2*y1*r)/n
        ans+=(abs(y1-y2)*r)/n
    
    elif y1>y2:
        ans+=(abs(y1-y2)*r)/n
        #print(ans)
        if abs(x1-x2)*(pi/m)/2<=1.0:
            ans+=(abs(x1-x2)*(pi/m)*y2*r)/n
        else:
            ans+=(2*y2*r)/n
        #print(ans)
    
    else:
        
        if abs(x1-x2)*(pi/m)/2<=1.0:
            ans+=(abs(x1-x2)*(pi/m)*y1*r)/n
        else:
            ans+=(2*y2*r)/n
        #print(ans)
    return ans
    
    
def main():
    m,n,r=map(float,input().split())
    m,n=int(m),int(n)
    x1,y1,x2,y2=map(int,input().split())
    ans=calc(m,n,r,x1,y1,x2,y2)
    print(str(round(ans,14)))    
    

main()