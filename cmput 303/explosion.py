
def probabilty(good,bad,d,memo,key):
    if key in memo:
        return memo[key]
        
    prob=[]
    for i in range(1,7):
        if good[i]<=0:
            pass
        else:
            good[i-1],good[i]=good[i-1]+1,good[i]-1
            ans=calc(good,bad,d-1,memo)
            good[i-1],good[i]=good[i-1]-1,good[i]+1
            prob.extend(good[i]*[ans])
    
    #print(prob)
    for i in range(1,7):
        if bad[i]<=0:
            pass
        else:
            bad[i-1],bad[i]=bad[i-1]+1,bad[i]-1
            ans=calc(good,bad,d-1,memo)
            bad[i-1],bad[i]=bad[i-1]-1,bad[i]+1
            prob.extend(bad[i]*[ans])
    #print(prob)       
    if len(prob)!=0:
        ans=sum(prob)/len(prob)
    else:
        ans=0
    
    memo[key]=ans
    return ans    
        
    
def calc(good,bad,d,memo):
    key=(tuple(good),tuple(bad),d)
    if key in memo:
        return memo[key]
        
    temp_sum0=0
    for i,j in enumerate(bad):
        temp_sum0+=(i*j)
    if temp_sum0>d:
        memo[key]=0.0
        return 0.0
    
    temp_sum1=0
    for i in bad[1:]:
        temp_sum1+=i
    if temp_sum1==0:
        memo[key]=1.0
        return 1.0
        
    
    ans=probabilty(good,bad,d,memo,key)
    return ans
    
def main():
    n,m,d=map(int,input().split())
    good,bad=[0]*7,[0]*7
    
    g=list(map(int,input().split()))
    for i in g:
        good[i]+=1

    b=list(map(int,input().split()))
    for i in b:
        bad[i]+=1
    
    ans=calc(good,bad,d,memo={})
    print(round(ans,10))
main()