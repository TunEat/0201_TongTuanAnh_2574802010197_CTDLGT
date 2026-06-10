a = [
    (2,'a'),
    (1,'b'),
    (2,'c'),
    (4,'d'),
    (3,'o')
]
def sapxep(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j][0] > a[j+1][0]:
                a[j],a[j+1] = a[j+1],a[j]
            
    return a
print(sapxep(a))