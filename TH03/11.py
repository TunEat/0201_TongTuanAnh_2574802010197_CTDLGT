def tangdan(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if abs[j] > abs[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    
    print(a)
a = [-3,1,-2,2]
tangdan(a)