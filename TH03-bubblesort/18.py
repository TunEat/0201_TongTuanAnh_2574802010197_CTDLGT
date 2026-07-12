def sapxep(a):
    dem = 0
    for i in range(len(a)):
        doi = False
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                doi = True
        if doi:
            dem += 1
        else:
            break
    print(a)
    print(f'{dem} luot')


a = [1,2,3,5,4]
sapxep(a)