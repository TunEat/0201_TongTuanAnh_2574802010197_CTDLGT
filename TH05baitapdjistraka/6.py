#bài 6
import heapq

def shortest_path(graph, s, t):
    n = len(graph)

    dist = [float('inf')] * n
    dist[s] = 0

    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)

        if u == t:
            return dist[t]

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            nd = dist[u] + w

            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return -1

graph = {
    0:[(1,4),(2,1)],
    1:[(3,1)],
    2:[(1,2),(3,5),(4,8)],
    3:[(4,3),(5,6)],
    4:[(5,2)],
    5:[]
}

print(shortest_path(graph,0,4))