
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