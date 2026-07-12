#bài 13
adj = [
    [(1, 4), (2, 1)],
    [(3, 1)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3), (5, 6)],
    [(5, 2)],
    []
]
def count_shortest_paths(adj, s):
    n = len(adj)

    dist = [float('inf')] * n
    ways = [0] * n
    visited = [False] * n

    dist[s] = 0
    ways[s] = 1

    for i in range(n):
        u = -1
        minn = float('inf')

        for j in range(n):
            if not visited[j] and dist[j] < minn:
                minn = dist[j]
                u = j

        if u == -1:
            break

        visited[u] = True

        for v, w in adj[u]:

            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                ways[v] = ways[u]

            elif dist[v] == dist[u] + w:
                ways[v] += ways[u]

    return dist, ways

dist, ways = count_shortest_paths(adj, 0)

print("Dist =", dist)
print("Ways =", ways)