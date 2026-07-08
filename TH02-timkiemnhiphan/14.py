a = [
    [1, 3, 5],
    [7, 9, 11]
]

def timkiem(a, x):
    for i in range(len(a)):          
        for j in range(len(a[i])):   
            if a[i][j] == x:
                return True
    return False

print(timkiem(a, 9))