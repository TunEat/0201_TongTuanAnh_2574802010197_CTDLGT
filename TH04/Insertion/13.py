#tính ổn định 
def sapxep(a):
    for i in range(1,len(a)):
        b = a[i]
        j = i-1
        while j >= 0 and a[i][0] < a[j][0]:
            a[j+1]=a[j]
            j -=1
        a[j+1] = b
    print(a)

a = [
    (2,'a'),
    (1,'b'),
    (2,'c')
]    
sapxep(a)
