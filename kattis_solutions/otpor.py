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
connection=['-','|']

def series(sub):
    ans=sum(r for r in sub if r not in connection)
    return ans
    
def parallel(sub):
    ans=sum(1.0/r for r in sub if r not in connection)
    return 1.0/ans
    
def solve(res):
    stack = []
    exp=input()
    for i in exp:
        if i =='(':
            stack.append(i)
        elif i.isdigit():
            stack.append(res[int(i)-1])
        elif i in connection:
            stack.append(i)
        elif i=='(':
            stack.append(i)
        elif i==')':
            sub=[]
            while stack and stack[len(stack)-1]!='(':
                sub.append(stack.pop())
            stack.pop()
            
            if '|' in sub:
                #print(sub)
                ans=parallel(sub)
            elif '-' in sub:
               ans=series(sub)
            stack.append(ans)
    if stack:
        return stack[0]  
    else: return 0

def main():
    cases=int(input())
    inp=list(map(float,input().split()))
    #print(inp)
    result=solve(inp)
    print(f"{result:.6f}")
    
main()