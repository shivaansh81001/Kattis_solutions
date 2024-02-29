'''

  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/hopcroft_karp.py

'''
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

def main():
    n,m = map(int, input().split())
    graph=[]
    for i in range(n):
       temp=[]
       graph.append(temp)

    for i in range(n):
        inp=list(map(int, input().split()))
        for j in inp[1:]:
            graph[i].append(j-1)

    print(hopcroft_karp(graph,n,m))

main()