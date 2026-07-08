#bài 15 tìm số nguyên tố đầu tiên
def nguyen_to():
    ds = []
    for i in range(n):
        c= True
        for j in range(2,a[i]):
            if a[i] % j == 0:
                c = False
                break
            
        if c == True:
            ds.append(a[i])
    print(f"Số nt đầu tiên và vị trí là {ds[0]} và {i}")

a = [4,6,8,10,11,13]    
n = len(a)
nguyen_to()