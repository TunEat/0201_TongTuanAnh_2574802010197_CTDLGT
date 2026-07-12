#bai 17
def b(w, D, sucChua):
    ngay = 1
    tong = 0

    for i in w:
        if tong + i <= sucChua:#kiem tra xem co vuot khoi luong ko
            tong += i
        else:#neu vuot khoi luong thi chuyen qua ngay tiep theo
            ngay += 1
            tong = i

    return ngay <= D#true hoac false

def a(w, D):
    left = max(w)#phan tu lon nhat  #10
    right = sum(w)#tinh tong #55

    while left < right:
        mid = (left + right) // 2

        if b(w, D, mid):#true thi chay code ben trong
            right = mid
        else:#false thi chay
            left = mid + 1

    return left

w = [1,2,3,4,5,6,7,8,9,10]
D = 5
print(a(w, D))