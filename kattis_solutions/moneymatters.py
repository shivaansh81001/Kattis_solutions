
'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
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