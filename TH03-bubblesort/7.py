#bài 7 sắp xếp mảng ký tự
def sapxep(a):
    ds = ['a','b','c','d']
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] != ds[j]:
                a[j],a[j+1] = a[j+1],a[j]
    print(a)
a = ['d','a','c','b']
sapxep(a)