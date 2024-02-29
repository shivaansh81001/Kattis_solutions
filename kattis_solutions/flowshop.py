
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