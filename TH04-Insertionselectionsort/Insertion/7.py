#sắp xếp các mảng chữ cái
def sapxep(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -=1
        a[j+1] = key
            

a = ['d','a','c','b']
sapxep(a)
print(a)