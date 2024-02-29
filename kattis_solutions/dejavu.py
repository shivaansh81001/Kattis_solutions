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
def calc(dp,cases):
    ans=0
    x=dict()
    y=dict()
    for i in range(cases):
        x[dp[0][i]],y[dp[1][i]]=x.get(dp[0][i],0)+1,y.get(dp[1][i],0)+1
    #print(x,y)
    for j in range(cases):
        ans+=(x[dp[0][j]]-1)*(y[dp[1][j]]-1)
    return ans
    
def main():
    cases=int(input())
    dp=[]
    for i in range(2):
        temp=[]
        for j in range(cases):
            temp.append(0)
        dp.append(temp)
    #print(dp)
    for i in range(cases):
        dp[0][i],dp[1][i]=map(int,input().split())
    #print(dp)
    ans=calc(dp,cases)
    print(ans)
main()