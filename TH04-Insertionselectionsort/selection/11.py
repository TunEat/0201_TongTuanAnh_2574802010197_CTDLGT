#bài 11 tính không ổn định 
def sapxep(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[min][0] > a[j][0]:
                min = a[j][0]
        a[i],a[min]=a[min],a[i]
    print(a)
a = [(2,'a'),(2,'b'),(1,'c')]
sapxep(a)

