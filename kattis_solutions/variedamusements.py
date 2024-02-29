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
p=10**9+7
def calc(dp, n, a, b, c):
    ans=0
    for i in range(1,n):
        dp[i][0],dp[i][1],dp[i][2]=((dp[i-1][1]+dp[i-1][2])*a%p),((dp[i-1][0]+dp[i-1][2])*b%p),((dp[i-1][0]+dp[i-1][1])*c%p)
    #print(dp)
    ans+=sum(dp[n-1])%p
    return ans

def main():
    n,a,b,c=map(int,input().split())
    dp=[]
    for i in range(n):
        temp=[]
        for j in range(3):
            temp.append(0)
        dp.append(temp)
    dp[0]=[a,b,c]
    #print(dp)
    ans=calc(dp,n,a,b,c)
    print(ans)
main()