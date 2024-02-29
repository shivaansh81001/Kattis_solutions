
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