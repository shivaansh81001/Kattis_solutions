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

def sums(dp,m,n,memo):
    #print(m,n)
    if m>=0 and n>=0:
        if m==0 and n==0:
            return dp[0][0]
        if memo[m][n]!=-1:
            return memo[m][n]
        
        total_sum=dp[m][n]+max(sums(dp,m-1,n,memo),sums(dp,m,n-1,memo))
        
        memo[m][n]=total_sum
        return total_sum
    
    else:
        return float('-inf')    


def main():
    m,n=map(int,input().split())
    #p1,p2,p3=map(int,input().split())
    #q1,q2,q3=map(int,input().split())
    dp=[]
    memo=[]
    for i in range(m):
        temp=[]
        for j in range(n):
            temp.append(-1)
        memo.append(temp)
        #temp=[]
        # j in range(n):
            #temp.append(0)
        #dp.append(temp)
        dp.append(list(map(int,input().split())))
    #print(dp)
    #print(memo)
    for i in range(m):
        print(sums(dp,i,n-1,memo),end=' ')
    
    #sums(dp,m,n)
    
main()