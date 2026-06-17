#bài 5 đếm số lần so sánh
def sapxep(a):
    count = 0
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min = j
                count += 1
        a[i],a[min]=a[min],a[i]
        
    print(a)
    print(count)

a = [3,2,1]
#[2,3,1]
#[2,1,3]
#[1,2,3]
sapxep(a)