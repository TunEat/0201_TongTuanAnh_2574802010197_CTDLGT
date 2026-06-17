#sắp xếp chuỗi theo độ dài
def sapxep(a):
    for i in range(0,len(a)):
        b = a[i]
        j = i -1
        while j >= 0 and len(a[j]) >len(a[j+1]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = b
        
    print(a)
a = ['abc','a','ab']
sapxep(a)    