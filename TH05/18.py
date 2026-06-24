#bài 18
import sys

class Graph17:
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(cung, L, a):
        print(f"--- Kết quả Bài 17 Bottleneck (Đỉnh nguồn từ: {a}) ---")
        for nut in range(cung.x):
            if L[nut] == sys.maxsize:
                print(a, "đến đỉnh", nut, "cạnh lớn nhất là: Không có đường đi")
            else:
                print(a, "đến đỉnh", nut, "cạnh lớn nhất trên đường đi là:", L[nut])

    def duongdinhonhat(cung, L, P):
        min_val = sys.maxsize
        min_index = -1
        for x in range(cung.x):
            if L[x] < min_val and P[x] == False:
                min_val = L[x]
                min_index = x
        return min_index

    def timduongdi(cung, a):
        L = [sys.maxsize] * cung.x
        L[a] = 0 
        P = [False] * cung.x

        for cout in range(cung.x):
            u = cung.duongdinhonhat(L, P)
            if u == -1: break
            P[u] = True

            for x in range(cung.x):
                if cung.graph[u][x] > 0 and P[x] == False:
                    cung_lon_nhat = max(L[u], cung.graph[u][x])
                    if L[x] > cung_lon_nhat:
                        L[x] = cung_lon_nhat
                        
        cung.inketqua(L, a)

# --- PHẦN KHỞI TẠO VÀ CHẠY THỬ ---
g = Graph17(3)
g.graph = [
    [0, 10, 3], # Đi thẳng từ 0 -> 1 mất cạnh nặng 10. Đi 0 -> 2 mất cạnh nặng 3.
    [10, 0, 1], # Đi tiếp từ 2 -> 1 mất cạnh nặng 1.
    [3, 1, 0]
]

g.timduongdi(0) # Kết quả từ 0 -> 1 sẽ chọn đường qua đỉnh 2 để bottleneck chỉ là 3 thay vì 10