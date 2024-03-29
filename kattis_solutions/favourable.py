
import sys

def outcome(key, dictn, memo):
    #print(dictn,memo)
    if key in memo:
        return memo[key]
    a = 0
    if type(dictn.get(key))==list:
        for i in dictn.get(key):
            if dictn[i]=='favourably':
                a+=1
            elif dictn[i]=='catastrophically':
                a+=0
            else:
                #print(key,dictn.get(key),i)
                a+=outcome(i,dictn,memo)
    else:
        if dictn[key]=='favourably':
            #print('yes')
            a+=1
        elif dictn[key] == 'catastrophically':
            #print('no')
            a+=0
    memo[key]=a
    #print(a)
    return a
    
def main():
    sys.setrecursionlimit(100000)
    cases=int(input())
    dictn={}
    
    for i in range(cases):
        S=int(input())
        
        for j in range(S):
            inp=input().split()
            if len(inp)==4:
                inp=[eval(x) for x in inp]
                dictn[inp[0]]=inp[1:]
            else :
                dictn[int(inp[0])]=inp[1]
        ans=0
        memo={}
        #print(dictn)
        
        #print('new-----')
        
        temp=outcome(1,dictn,memo)
    
        print(temp)
            
        

main()