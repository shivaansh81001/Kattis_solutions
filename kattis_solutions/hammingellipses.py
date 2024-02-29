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

def no_match(dp,q,i,j):
    #print(q)
    if j>=1:
        dp[i][j]=2*(dp[i-1][j-1])
    if j>=2:
        dp[i][j]+=((q-2)*(dp[i-1][j-2]))
    #view(dp)
    
def calc(dp,q,n,d,s1,s2):
    #print(dp)
    for i in range(1,n+1):
        for j in range(d+1):
            if s1[i-1]==s2[i-1]:
                dp[i][j]=dp[i-1][j]
                if j<2:
                    pass
                else:
                    dp[i][j]+=(dp[i-1][j-2])*(abs(1-q))
            else:
                no_match(dp,q,i,j)
    #view(dp)            
    return dp[n][d]

def view(dp):
    for i in range(len(dp)):
        for j in range(len(dp[1])):
            print(dp[i][j],end=' ')
        print("")
    return    

def main():
    q,n,d=map(int,input().split())
    s1=input()
    s2=input()
    dp=[]
    for i in range(n+1):
        temp=[]
        for j in range(d+1):
            temp.append(0)
        dp.append(temp)
    dp[0][0]=1
    #view(dp)
    ans=calc(dp,q,n,d,s1,s2)
    print(ans)
main()