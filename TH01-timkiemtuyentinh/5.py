#bài 9 Tìm tất cả vị trí
def tim_tat_ca(a,n,x):
    c = []
    for i in range(0,n):
        if a[i] == x:
            c.append(i)
    print(f"Vi tri cua {x} trong danh sach lan luot la {c}")

a = [4,14,4,2,4]
x = 4
n = len(a)
tim_tat_ca(a,n,x)
