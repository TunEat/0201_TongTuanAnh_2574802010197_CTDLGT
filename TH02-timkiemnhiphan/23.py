#bài 23 phần tử nhỏ thứ k trong ma trận sắp xếp
a=[
    [1,5,9],
    [10,11,13],
    [12,13,15]
]
def phantu(a,k):
    ds = []
    for i in range(len(a)):
        for j in range(len(a)):
            ds.append(a[i][j])   
    print(ds[k-1])
    
phantu(a,9)
