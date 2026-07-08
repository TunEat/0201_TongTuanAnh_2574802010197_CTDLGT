#bài 18 tìm kiếm trên ma trận hai chiều
mt = [  
    [5,8,1],
    [3,9,7,],
    [2,6,4]
]

def matran(mt,x):
    for i in range(len(mt)):
        for j in range(len(mt[i])):
            if mt[i][j] == x:
                return (i,j)
    return (-1,-1)
print(matran(mt,9))