def timkiem(a,x):
    for i in range(len(a)):
        if a[i] == x: #so sánh coi có bằng không
            return True #trả về True
    return False #trả về False



a = [2,4,6,8]
print(timkiem(a,2))    