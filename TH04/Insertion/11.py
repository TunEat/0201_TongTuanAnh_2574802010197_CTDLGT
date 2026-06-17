#sắp xếp theo trị tuyệt đối (ổn định)
def sapxep(a):
    for i in range(len(a)):
        if a[i] < 0:
            a[i] = -a[i]
        b = a[i]
        j = i-1
        while j >= 0 and b < a[j]:
            a[j+1] = a[j]
            j-= 1
        a[j+1] =b 
    print(a)


a = [-3,1,-2,2]
sapxep(a)    