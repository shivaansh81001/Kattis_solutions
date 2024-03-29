'''

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