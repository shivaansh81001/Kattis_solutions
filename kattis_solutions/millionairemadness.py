'''
  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/dijkstra.py

'''
from heapq import heappop, heappush

directions=[(1,0),(0,-1),(0,1),(-1,0)]

def valid_x(next_x,r,c):
    if 0<=next_x<r:
        return True
    return False
    
def valid_y(next_y,r,c):
    if 0<=next_y<c:
        return True
    return False
    
def dijkstra(graph,m,n, start=(0,0)):
    """ 
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    r,c=m,n
    dist= [[float("inf")]*c for i in range(r)] 
    dist[start[0]][start[1]] = 0

    queue = [(0,0,0)]
    while queue:
        length,x,y = heappop(queue)
        if x==r-1 and y==c-1:
            return length
        else:
            
            for tx,ty in directions:
                next_x=x+tx
                next_y=y+ty
                if valid_x(next_x,r,c)==True and valid_y(next_y,r,c)==True:
                    n_length=max(length,max(graph[next_x][next_y]-graph[x][y],0))
                    if n_length<dist[next_x][next_y]:
                        dist[next_x][next_y]=n_length
                        heappush(queue,(n_length,next_x,next_y))
                    

    return dist[r-1][c-1]
    
def main():
    m,n=map(int,input().split())
    graph=[]
    for i in range(m):
        graph.append(list(map(int,input().split())))
        
    print(dijkstra(graph,m,n))
    
main()