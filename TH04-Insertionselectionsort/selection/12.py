#bài 12 selection sort ổn định
def sapxep(a):
    for i in range(len(a)):
        min = a[i][0]
        for j in range(i+1,len(a)):
            if a[min] > a[j][0]:
                min = a[j][0]
        a[i],a[min]=a[min],a[i]
    print(a)


a = [(2,'a'),(1,'b'),(2,'c')]
sapxep(a)    