#bài 10 đếm chính xác số swap
def sapxep(a):
    count = 0
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min = j
                count +=1 
        a[i],a[min] = a[min],a[i]
    print(a)
    print(f'so lan swap là {count}')
a= [1,2,3]
sapxep(a)    