def chen(a,x):
    for i in range(len(a)):
        if a[i] > x:
            print(f'Vị trí mà {x} chèn vào là {i}')
            break
a = [1,3,5,6]
chen(a,4)