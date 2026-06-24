#bài 14
adj = [
    [(1, 4), (2, 1)],
    [(3, 1)],
    [(1, 2), (3, 5), (4, 8)],
    [(4, 3), (5, 6)],
    [(5, 2)],
    []
]
def second_shortest(adj, start, end):
    n = len(adj)

    first = [float('inf')] * n
    second = [float('inf')] * n

    first[start] = 0

    for _ in range(n * n):

        updated = False

        for u in range(n):

            for v, w in adj[u]:

                nd = first[u] + w

                if nd < first[v]:

                    second[v] = first[v]
                    first[v] = nd
                    updated = True

                elif first[v] < nd < second[v]:

                    second[v] = nd
                    updated = True

        if not updated:
            break

    return second[end]

print(second_shortest(adj, 0, 4))