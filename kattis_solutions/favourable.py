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