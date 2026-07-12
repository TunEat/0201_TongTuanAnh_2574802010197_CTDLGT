#bài 4 in mảng sau mỗi vòng chọn 
def sapxep(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min = j
        a[i],a[min] =a[min],a[i]
        print(a)


a = [3,1,2]
sapxep(a)    