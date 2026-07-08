#bài 13 tìm kiếm trên chuỗi
def timkiem(a,n,x):
    for i in range(n):
        if a[i].lower() == x.lower():
            return i
    return -1
   
a = ["An","Bình","Châu"]
n = len(a)
print(timkiem(a,n,"an"))