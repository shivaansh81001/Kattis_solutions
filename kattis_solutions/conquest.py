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
sys.setrecursionlimit(1000000)

def dfs(start,graph,army_size,visited,army):
    #print('start',start)
    visited[start]=True
    temp=army
    #print(temp,start)
    islands=list()
    if start not in graph:
        pass
    else:
        islands=graph[start]
    islands=sorted(islands,key=lambda x:army_size[x])
    #print('islands',islands)
    i=0
    while i<len(islands):
        if visited[islands[i]]:
            pass
        else:
            if army_size[islands[i]]>=temp:
                pass
                
            else:
                temp+=army_size[islands[i]]
                temp=dfs(islands[i],graph,army_size,visited,temp)
        i+=1
            
    return temp

def main():
    N, M = map(int, input().split())
    graph={}
    for i in range(1,N+1):
        graph[i]=[]

    for j in range(M):
        x,y=map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    #print(graph)
    
    army_size=[0]*(N+1)
    for k in range(1,N+1):
        army_size[k]=int(input())
    visited=[False]*(N+1)
    start=1
    start_army=army_size[1]
    ans=dfs(start,graph,army_size,visited,start_army)

    print(ans)

if __name__ == "__main__":
    main()