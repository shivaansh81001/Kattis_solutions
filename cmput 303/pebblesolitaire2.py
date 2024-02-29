
import time
def check_right(i,inp):
    if inp[i]=='o' and inp[i+1]=='o' and inp[i+2]=='-':
        return True
    return False
def change_right(i,inp):
    f=inp[:i]
    s="--o"
    t=inp[i+3:]
    return f+s+t
    
def check_left(i,inp):
    if inp[i]=='-' and inp[i+1]=='o' and inp[i+2]=='o':
        return True
    return False
def change_left(i,inp):
    f=inp[:i]
    s="o--"
    t=inp[i+3:]
    return f+s+t   
    
def solve(memo,inp):
    #time.sleep(2)
    if inp in memo:
        return memo[inp]
    cnt=0
    n=len(inp)
    #print(inp)
    for i in inp:
        if i=='o':
            cnt+=1
    
    for i in range(n-2):
        if check_right(i,inp):
            temp=change_right(i,inp)
            cnt=min(cnt,solve(memo,temp))
    
    for i in range(n-2):
        if check_left(i,inp):
            temp=change_left(i,inp)
            cnt=min(cnt,solve(memo,temp))
    #print('hi')  
    memo[inp]=cnt
    return cnt

def main():
    cases=int(input())
    for i in range(cases):
        inp=input()
        memo=dict()
        ans=solve(memo,inp)
        print(ans)
        
main()