
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