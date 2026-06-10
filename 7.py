def lonnhat(a,x):
    for i in range(len(a)):
        if a[i] > x:       
            print(f'Vị trí phần tử nhỏ nhất lớn hơn {x} là {a[i]}')
            break
a = [1,3,5,7]
lonnhat(a,5)    