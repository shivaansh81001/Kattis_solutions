
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