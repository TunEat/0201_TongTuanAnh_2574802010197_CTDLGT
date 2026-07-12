#đếm số lần dịch chuyển
def solan(a):
    dem = 0
    for i in range(1,len(a)):
        b = a[i]
        j = i -1
        while j >= 0 and b < a[j]:
            a[j+1] = a[j]
            j-=1
            dem += 1
        a[j+1] = b
    print(a)
    print(dem)

a = [3,2,1]
solan(a)

