#bài 7
import heapq

def dijkstra_path(graph, s, t):
    n = len(graph)

    dist = [float('inf')] * n
    parent = [-1] * n

    dist[s] = 0

    pq = [(0,s)]

    while pq:
        d,u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v,w in graph[u]:
            nd = dist[u] + w

            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq,(nd,v))

    path = []
    cur = t

    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    return path, dist[t]

graph = {
    0:[(1,4),(2,1)],
    1:[(3,1)],
    2:[(1,2),(3,5),(4,8)],
    3:[(4,3),(5,6)],
    4:[(5,2)],
    5:[]
}

path, cost = dijkstra_path(graph,0,4)

print(path)
print(cost)