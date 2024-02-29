'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -https://docs.python.org/3/library/collections.html#collections.deque

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
'''
from collections import deque

def graph(countries,before,after,links,L,X):
    if L==X:
        countries[X]='leave'
        return
    deq=deque([L])
    countries[L]='leave'
    while deq:
        temp=deq.popleft()
        #print(temp)
        for i in links[temp]:
            #print(i)
            if countries[i]!='leave':
                after[i-1]=after[i-1]-1
                if after[i-1]>before[i-1]//2:
                    pass
                else:
                    countries[i]='leave'
                    deq.append(i)
def main():
    countries={}
    
    C,P,X,L=map(int,input().split())
    links={}
    
    for i in range(1,C+1):
        countries[i]='stay'
        links[i]=[]
    #print(countries)
    before=[0]*C
    after=[0]*C
    
    
    for i in range(P):
        temp=input().split()
        for j in temp:
            before[int(j)-1]+=1
            after[int(j)-1]+=1
        links.get(int(temp[0])).append(int(temp[1]))
        links.get(int(temp[1])).append(int(temp[0]))
    #print('before',before)
    #print(links)        
        
        
 
    #print('after',after)
    
    graph(countries,before,after,links,L,X)
    print(countries[X])
    
    
main()