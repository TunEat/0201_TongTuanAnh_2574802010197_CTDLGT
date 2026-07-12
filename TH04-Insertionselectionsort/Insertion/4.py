#bài 4 in mảng sau mỗi bước chèn
def sapxep(a):
    for i in range(1,len(a)):
        b = a[i]
        j = i-1
        while j >= 0 and b < a[j]:
            a[j+1] = a[j]
            j-= 1 
        a[j+1] = b
        print(a)

a = [3,1,2]    
sapxep(a)
