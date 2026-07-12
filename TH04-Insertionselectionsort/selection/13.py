#bài 13 sắp xếp đối tượng theo khóa
def sapxep(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[min][1] > a[j][1]:
                min = a[j][1]
        a[i],a[j]=a[j],a[i]
    print(a)

a = [('An',8),('Ba',5)]
sapxep(a)    