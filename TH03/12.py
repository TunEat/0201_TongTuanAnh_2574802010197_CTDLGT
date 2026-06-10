def sapxep(a):
    for i in range(len(a)):
        for j in range(len(a[i])-1):
            if len(a[j]) > len(a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    print(a)

a = ['abc','a','ab']
sapxep(a)