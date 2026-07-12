#bài sắp xếp tăng dần cơ bản
def sapxep(a):
    for i in range(1,len(a)):
        b = a[i]
        j = i -1
        while j >= 0 and b < a[j]:
            a[j+1] = a[j]
            j-= 1
        a[j+1] =b 



a = [5,2,4,6,1,3]
sapxep(a)
print(a)
