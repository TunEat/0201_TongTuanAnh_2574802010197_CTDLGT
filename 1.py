def vitri(a,x):
    for i in range(len(a)): 
        if a[i] == x: #a[i] giá trị tương đương với vị trí của i
            return i #trả về vị trí i
    return -1
    
a = [1,3,5,7,9]
print(vitri(a,7)) #print ra kết quả