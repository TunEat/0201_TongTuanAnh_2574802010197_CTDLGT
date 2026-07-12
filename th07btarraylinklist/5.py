a = []
def them(giatri):
    a.append(giatri)
def lap(a):
    lan = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            lan +=1
    print(f"so chan la {lan}")

them(1)
them(2)
them(3)
them(4)


lap(a)

