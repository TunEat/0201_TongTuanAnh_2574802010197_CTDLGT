#bài 8 Đếm số lần xuất hiện
def dem_xuat_hien(a,n,x):
    c = 0
    for i in range(0,n):
        if a[i] == x:
            c += 1
    print(f'So lan xuat hien cua {x} là ',c)
    
a=[2,5,2,7,2]
x = 2
n = len(a)
dem_xuat_hien(a,n,x)
