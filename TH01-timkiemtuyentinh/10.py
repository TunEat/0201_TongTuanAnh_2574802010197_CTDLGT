#bài 14 Tìm theo điều kiện
def sochanfirst(a,n):
    c = []
    for i in range(0,n):
        if a[i] % 2 == 0:
            c.append(a[i])
            break
    print(f'So chan dau tien va vi tri lan luot la {c} va {i}')

a = [3,7,11,8,5,4]
n = len(a)
sochanfirst(a,n)
