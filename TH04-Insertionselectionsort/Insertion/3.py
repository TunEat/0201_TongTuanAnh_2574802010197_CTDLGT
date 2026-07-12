#bài 3 sắp xếp giảm dần
def sapxep(a):
    for i in range(1,len(a)):
        b = a[i] #2 #4
        j = i -1#0 #1
        while j >= 0 and b > a[j]:#2>5 #4>2
            a[j+1] = a[j]
            j-= 1
        a[j+1] = b



a = [5,2,4,6,1]
sapxep(a)
print(a)
