#Thực hiện một lượt (one pass)
def tangdan(a):
    for i in range(1):
        for j in range(0,len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

a = [5,1,4,2,8]    
print(tangdan(a))