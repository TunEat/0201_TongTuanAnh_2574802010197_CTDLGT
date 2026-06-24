#bài 16
import sys

class Graph16:
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]
        cung.chi_phi_dinh = [0] * dinh 

    def inketqua(cung, L, a):
        print(f"--- Kết quả Bài 16 (Đỉnh nguồn từ: {a}) ---")
        for nut in range(cung.x):
            print(a, "đến đỉnh", nut, "độ dài đường đi là:", L[nut])

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
        L[a] = cung.chi_phi_dinh[a] 
        P = [False] * cung.x

        for cout in range(cung.x):
            u = cung.duongdinhonhat(L, P)
            if u == -1: break
            P[u] = True

            for x in range(cung.x):
                if cung.graph[u][x] > 0 and P[x] == False:
                    chi_phi_moi = L[u] + cung.graph[u][x] + cung.chi_phi_dinh[x]
                    if L[x] > chi_phi_moi:
                        L[x] = chi_phi_moi
                        
        cung.inketqua(L, a)

# --- PHẦN KHỞI TẠO VÀ CHẠY THỬ ---
g = Graph16(3)
g.chi_phi_dinh = [10, 20, 5]  # Chi phí để đi qua đỉnh 0 là 10, đỉnh 1 là 20, đỉnh 2 là 5
g.graph = [
    [0, 5, 0],  # Đường đi từ 0 -> 1 tốn 5 chi phí cạnh
    [5, 0, 2],  # Đường đi từ 1 -> 2 tốn 2 chi phí cạnh
    [0, 2, 0]
]

g.timduongdi(0)