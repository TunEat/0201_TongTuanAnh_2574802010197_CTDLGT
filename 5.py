def dem(a,x):
    c = 0 #gán c = 0 để đếm
    for i in range(len(a)): #lặp dựa vào số phần tử trong mảng
        if a[i] == x: #nếu đúng
            c = c + 1 #gán c += 1
    print(f'Só lần xuất hiện của {x} là {c}')
    
a = [1,2,2,2,3]
dem(a,2)