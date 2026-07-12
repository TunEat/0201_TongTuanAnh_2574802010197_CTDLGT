# sắp xếp đối tượng theo nhiều khóa
a = [
    ('An',8),
    ('Ba',9),
    ('Cu',8)
]
def sapxep(a):
    for i in range(1,len(a)):
        b = a[i]
        j = i-1
        while j >= 0:
            if a[i][1] < a[j][1]:
                a[j+1] = a[j]
                j -= 1
        a[j+1] = b
    print(a)
sapxep(a)