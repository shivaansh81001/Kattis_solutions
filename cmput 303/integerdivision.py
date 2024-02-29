
def calc(nums,m):
    ans=0
    for i in nums:
        if i in m:
            m[i]=m[i]+1
        else:
            m[i]=1
    #print(m)
    for i in m.values():
        ans+=(((i-1)*i)//2)
    
    print(ans)
    
def main():
    n,d = map(int,input().split())
    nums=list(map(int,input().split()))
    #print(nums)
    for i in range(n):
        nums[i]=nums[i]//d
    #print(nums)
    m=dict()    
    calc(nums,m)
    
    
main()