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