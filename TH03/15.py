a = [
    ('Cu',8),
    ('Ba',9),
    ('An',8)
]
def sapxep(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j][1] < a[j+1][1]:
                a[j],a[j+1]=a[j+1],a[j]
            elif a[j][1] == a[j+1][1]:
                if a[j][0] > a[j+1][0]:
                    a[j],a[j+1] = a[j+1],a[j]
    return a
print(sapxep(a))