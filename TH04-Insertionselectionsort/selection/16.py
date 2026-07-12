#bài 16 sắp xếp theo trị tuyệt đối
def sapxep(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            x = a[min]
            y= a[j]
            if x<0:
                x=-a[min]
            if y<0:
                y=-a[j]
            if x >y:
                min = j
                
        a[i],a[min]=a[min],a[i]
    print(a)

a =[-3,1,-2,2]
sapxep(a)    