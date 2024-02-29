

import sys 
from heapq import heappush,heappop


def energy(graph,n,before,visited):
    ans=0
    temp=len(before)
    while temp<n:
        #print(temp)
        if len(q)!=0:
            dist,cur=heappop(q)
            #print(dist,curr)
            if not visited[cur]:
                temp=temp+1
                visited[cur]=True
                ans+=dist
            else:continue
            for j,k in graph[cur]:
                #print(j,k)
                if visited[k]:
                    pass
                else:
                    heappush(q,(j,k))
    return ans

def calc(graph,n,before):
    global q
    q=[]
    visited=[False]*n
    for i in before:
        visited[i]=True
        for j,k in graph[i]:
            if visited[k]:
                pass
            else:heappush(q,(j,k))
    #print(visited,q)           
    sys.stdout.write(str(energy(graph,n,before,visited))+'\n')
    
def main():
    cases=int(sys.stdin.readline().strip())
    for i in range(cases):
        n,m,l,s=map(int,sys.stdin.readline().split())
        before=[]
        for i in sys.stdin.readline().split():
            before.append(int(i)-1)
        #print(before)
        
        graph=[]
        for i in range(n):
            temp=[]
            graph.append(temp)
        #print(graph)
        
        for i in range(m):
            t1,t2,e=map(int,sys.stdin.readline().split())
            graph[t1-1].append((e+l,t2-1)),graph[t2-1].append((e+l,t1-1))
        #print(graph)
        calc(graph,n,before)
main()