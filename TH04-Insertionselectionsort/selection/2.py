#bài 2 sắp xếp tăng dần cơ bản
def sapxep(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min = j
        a[i],a[min]=a[min],a[i]
    print(a)


a = [5,2,4,6,1,3]
sapxep(a)