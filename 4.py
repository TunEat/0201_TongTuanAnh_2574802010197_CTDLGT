def timkiem(a,x):
    for i in range(len(a)):
        if a[i] == x:
            c = i
        #lúc này nó sẽ xét hết những giá trị bằng với x 
        #sau đó gán c = i là vị trí cuối cùng của x
    print(f"Vị trí cuối cùng của {x} là {c}")
a = [1,2,2,2,3]
timkiem(a,2)