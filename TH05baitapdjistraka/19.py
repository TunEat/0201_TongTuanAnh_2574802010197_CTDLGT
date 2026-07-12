#bài 19
class Graph19:
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0.0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(cung, L, a):
        print(f"--- Kết quả Bài 19 Xác suất (Đỉnh nguồn từ: {a}) ---")
        for nut in range(cung.x):
            print(a, "đến đỉnh", nut, "xác suất lớn nhất là:", round(L[nut], 4))

    def duongdixacsuatlonnhat(cung, L, P):
        max_val = -1.0
        max_index = -1
        for x in range(cung.x):
            if L[x] > max_val and P[x] == False:
                max_val = L[x]
                max_index = x
        return max_index

    def timduongdi(cung, a):
        L = [0.0] * cung.x 
        L[a] = 1.0          
        P = [False] * cung.x

        for cout in range(cung.x):
            u = cung.duongdixacsuatlonnhat(L, P)
            if u == -1: break
            P[u] = True

            for x in range(cung.x):
                if cung.graph[u][x] > 0.0 and P[x] == False:
                    tich_xac_suat = L[u] * cung.graph[u][x]
                    if L[x] < tich_xac_suat:
                        L[x] = tich_xac_suat
                        
        cung.inketqua(L, a)

# --- PHẦN KHỞI TẠO VÀ CHẠY THỬ ---
g = Graph19(3)
g.graph = [
    [0.0, 0.5, 0.9], # Đi thẳng từ 0 -> 1 xác suất thành công là 0.5. Đi từ 0 -> 2 là 0.9.
    [0.5, 0.0, 0.8], # Đi tiếp từ 2 -> 1 là 0.8.
    [0.9, 0.8, 0.0]
]

g.timduongdi(0) # Kết quả đi vòng 0 -> 2 -> 1 cho xác suất cao hơn (0.9 * 0.8 = 0.72) so với đi thẳng (0.5)