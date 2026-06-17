#bài 1 chèn một phần tử vào mảng đã sắp xếp
def chen(a,x):
    a.append(x)
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]


a = [1,3,5,7]
chen(a,4)
print(a)