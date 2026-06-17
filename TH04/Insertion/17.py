#bài 17 mảng gần như đã sắp xếp
def sapxep(a):
    count = 0
    for i in range(1,len(a)):
        b = a[i]
        j = i - 1
        while j >= 0 and b < a[j]:
            a[j+1] = a[j]
            j -= 1
            count += 1
        a[j+1] = b
    print(a)
    print(f'Chỉ {count} shift')

a = [1,2,4,3,5]    
sapxep(a)