def timkiem(a,x):
    for i in range(len(a)):
        if a[i] == x:
            print(f'Vị trí của {x} là {i}')
            break
a = [4,5,6,7,0,1,2]
timkiem(a,0)