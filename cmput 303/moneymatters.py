
'''
  
  -https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

'''

def dfs(graph, start,money):
    a=0
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            a+=money[vertex]
            stack.extend(graph[vertex] - visited)
    return a,visited
    
def main():
    
    n,m=map(int,input().split())
    money={}
    graph={}
    people=set()
    
    #visited={}
    
    for i in range(n):
        money[i]=int(input())
        graph[i]=set()
        people.add(i)
        
        #visited[i]='unvisited'
    #print(money)    
    
        
    for j in range(m):
        temp=input().split()
        graph.get(int(temp[0])).add(int(temp[1]))
        graph.get(int(temp[1])).add(int(temp[0]))
    
    #print(people)
    #print(graph)
    
    temp=0

    while(len(people)!=0):
        #print('-----------') 
        #print(people,temp)
        ans,visited= dfs(graph,temp,money)
        
        
        temp=list(people)[0]
        
        if ans==0:
            pass
            
            
        else:
            print('IMPOSSIBLE')
            return
      
        people=people-visited
        
    print('POSSIBLE')
    return
    

    
    
main()