def sapxep(a,k):
    count = 0
    for i in range(k):
        count += 1
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print(a)
    print(count)

a = [3,1,4,1,5]
sapxep(a,2)  