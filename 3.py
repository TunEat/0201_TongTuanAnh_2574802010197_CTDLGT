def timkiem(a,x):
    for i in range(len(a)):
        if a[i] == x:
            c = i #gán c là i (i là vị trí)
            break #dừng vòng lặp
    print(f"Vị trí đầu tiên của {x} là {c}")
a = [1,2,2,2,3]
timkiem(a,2)