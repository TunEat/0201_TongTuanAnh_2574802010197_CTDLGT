#bài 11 Tìm giá trị lớn nhất
def lon_nhat(a,n):
    c = 0
    for i in range(0,n):
        if a[i] > c:
            c = a[i]
    print(f"Gia tri lon nhat va vi tri lan luot la {c} va {i}")
a = [13,43,3,56,9]
n = len(a)
lon_nhat(a,n)