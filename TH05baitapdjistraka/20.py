#bài 20
class Graph20:
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def tim_k_duongdi(cung, a, t, K):
        ket_qua_t = []
        hang_doi = [[0, a]]
        dem_so_lan = [0] * cung.x

        while len(hang_doi) > 0:
            hang_doi.sort(key=lambda item: item[0])
            khoang_cach, u = hang_doi.pop(0)

            dem_so_lan[u] += 1

            if u == t:
                ket_qua_t.append(khoang_cach)
                if len(ket_qua_t) == K:
                    break

            if dem_so_lan[u] > K:
                continue

            for x in range(cung.x):
                if cung.graph[u][x] > 0 and dem_so_lan[x] < K:
                    hang_doi.append([khoang_cach + cung.graph[u][x], x])

        print(f"--- Kết quả Bài 20 ({K} đường đi ngắn nhất từ {a} tới {t}) ---")
        print("Mảng độ dài các đường đi tìm được:", ket_qua_t)

# --- PHẦN KHỞI TẠO VÀ CHẠY THỬ ---
g = Graph20(3)
g.graph = [
    [0, 3, 5],
    [3, 0, 1],
    [5, 1, 0]
]

# Tìm K=3 đường đi ngắn nhất từ đỉnh 0 đến đỉnh 2
g.tim_k_duongdi(0, 2, 3)