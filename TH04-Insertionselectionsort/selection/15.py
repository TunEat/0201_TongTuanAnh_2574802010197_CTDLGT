#bài 15 sắp xếp một phần (k nhỏ nhất)
def sapxep(a,k):
    for i in range(k):
        min = i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min = j
        a[i],a[min]=a[min],a[i]
    print(a)


a = [5,3,1,4,2]
sapxep(a,2)