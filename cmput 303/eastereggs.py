'''

  -https://www.geeksforgeeks.org/binary-search/
  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/geometry/lines.py
  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/hopcroft_karp.py


'''
import math

def distance(p1, p2):
    return sum((a - b) * (a - b) for a, b in zip(p1, p2))**0.5

def hopcroft_karp(graph, n, m):
    """
    Maximum bipartite matching using Hopcroft-Karp algorithm, running in O(|E| sqrt(|V|))
    """
    match1 = [-1] * n
    match2 = [-1] * m
    result = 0
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in graph[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break

        pointer = [len(c) for c in graph]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = graph[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    result += 1
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()
    return result


def search(n,b,r,dist,low=0,high=1e20,prec=.00000001):
    while high-low>prec:
        mid=(low+high)/2
        graph=[]
        for i in range(r):
            graph.append([])
        for i in range(r):
            for j in range(b):
                if dist[i][j]<mid:
                    graph[i].append(j)
        if r+b-hopcroft_karp(graph,r,b)>=n:
            low=mid
        else:
            high=mid
    return low
    
def main():
    n,b,r=map(int,input().split())
    red,blue=[],[]
    for i in range(b):
        blue.append(tuple(map(float, input().split())))
    for i in range(r):
        red.append(tuple(map(float, input().split())))
    
    dist=[]
    for i in range(r):
        temp=[]
        for j in range(b):
            temp.append(distance(red[i],blue[j]))
        dist.append(temp)
    #print(dist)
    ans=search(n,b,r,dist)
    print(f"{ans:.7f}")

main()