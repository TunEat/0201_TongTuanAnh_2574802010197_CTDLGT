#bài 22 median của hai mảng đã sắp xếp
def median(a,b):
    c = []
    for i in a:
        c.append(i)
    for j in b:
        c.append(j)
    for k in range(len(c)):
        for l in range(len(c)-1): 
            if c[l] > c[l+1]:
                c[l],c[l+1]=c[l+1],c[l]
    trungvi = (c[0]+c[-1])/2
    print(c)
    print(trungvi)
median(a=[1,2],b=[3,4])