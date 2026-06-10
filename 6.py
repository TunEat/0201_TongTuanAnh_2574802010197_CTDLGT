def nhonhat(a,x):
    for i in range(len(a)):
        if a[i] >= x:
            break
    print(f'Vị trí phần tử nhỏ nhất lớn hơn {x} là {i}')

a = [1,3,5,7]
nhonhat(a,4)    