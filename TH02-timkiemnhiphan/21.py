#bài 21 chia mảng tổng lớn nhất nhỏ nhất
def check(a, k, gioiHan):
    dem = 1
    tong = 0

    for i in a:
        if tong + i <= gioiHan:
            tong += i
        else:
            dem += 1
            tong = i

    return dem <= k


def splitArray(a, k):
    left = max(a)
    right = sum(a)

    while left < right:
        mid = (left + right) // 2

        if check(a, k, mid):
            right = mid
        else:
            left = mid + 1

    return left


a = [7,2,5,10,8]
k = 2

print(splitArray(a, k))