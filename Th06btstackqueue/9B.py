# Bài 9: Duyệt đồ thị BFS bằng Queue
# BFS duyệt theo chiều rộng


from collections import deque


def BFS(graph,start):

    visited = set()   # Lưu các đỉnh đã đi qua

    queue = deque()


    queue.append(start)

    visited.add(start)



    while queue:


        node = queue.popleft()

        print(node,end=" ")



        # Duyệt các đỉnh kề
        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)




graph = {

    1:[2,3],
    2:[4],
    3:[5],
    4:[],
    5:[]
}



BFS(graph,1)