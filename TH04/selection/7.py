#bài 7 sắp xếp mảng ký tự 
def sapxep(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min = j
        a[i],a[min] = a[min],a[i]
    print(a)
                       



a = ['d','a','c','b']
sapxep(a)    