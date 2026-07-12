#bài 15 Dijkstra trên dưới(grid)
import math
import sys

class Graph():
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(cung, L, a):
        print("Đỉnh nguồn:", a)
        for nut in range(cung.x):
            print(a, "->", nut, "=", L[nut])

    def duongdinhonhat(cung, L, P):
        min = sys.maxsize

        for x in range(cung.x):
            if L[x] < min and P[x] == False:
                min = L[x]
                min_index = x

        return min_index

    def timduongdi(cung, a):
        L = [sys.maxsize] * cung.x
        L[a] = 0

        P = [False] * cung.x

        for count in range(cung.x):

            u = cung.duongdinhonhat(L, P)

            P[u] = True

            for x in range(cung.x):

                if (cung.graph[u][x] > 0 and
                    P[x] == False and
                    L[x] > L[u] + cung.graph[u][x]):

                    L[x] = L[u] + cung.graph[u][x]

        cung.inketqua(L, a)


g = Graph(9)

g.graph = [
#0 1 2 3 4 5 6 7 8
[0,3,0,1,0,0,0,0,0], #0
[1,0,1,0,5,0,0,0,0], #1
[0,3,0,0,0,1,0,0,0], #2
[1,0,0,0,5,0,4,0,0], #3
[0,3,1,1,0,1,0,2,0], #4
[0,0,1,0,5,0,0,0,1], #5
[0,0,0,1,0,0,0,2,0], #6
[0,0,0,0,5,0,4,0,1], #7
[0,0,0,0,0,1,0,2,0]  #8
]

g.timduongdi(0)