
import sys
import math
from collections import deque

l1,l2=deque(),deque()

def adjust(l1, l2):
    #print(l1,l2)
    while(1):
        if len(l1)>len(l2)+1:
            l2.appendleft(l1.pop())
        else:
            break
    #print(l1,l2)
    #print(len(l1),len(l2))
    while(1):
        if len(l2)>len(l1):
            l1.append(l2.popleft())
        else:
            break
    #print(l1,l2)

def next(action,n):
    #print(action,n)
    
    if action=='get':
        if len(l1)>n:
            sys.stdout.write(str(l1[n])+'\n')
        else:
            sys.stdout.write(str(l2[n-len(l1)])+'\n')
    elif action=='push_front':
        l1.insert(0,n)
        
        #print('front',len(l1),len(l2))
    elif action=='push_back':
        l2.append(n)
        
        #print('back',len(l1),len(l2))
    elif action=='push_middle':
        if len(l1)!=len(l2):
            l2.insert(0,n) 
        else:
            l1.append(n)
        
    
    adjust(l1,l2)
    
def main():
    cases=0
    for inp in sys.stdin:
        line=inp.split()
        if len(line)==1:
            cases=line[0]
        else:
            next(line[0],int(line[1]))
main()

