#bài 9 double selection sort
def sapxep(a):
    left = 0
    right = len(a) - 1
    while left < right:
        min = left
        max = left
        # Tìm vị trí nhỏ nhất và lớn nhất
        for i in range(left, right + 1):
            if a[i] < a[min]:
                min = i
            if a[i] > a[max]:
                max = i
        # Đưa nhỏ nhất về đầu
        a[left], a[min] = a[min], a[left]
        # Nếu phần tử lớn nhất bị đổi vị trí
        if max == left:
            max = min
        # Đưa lớn nhất về cuối
        a[right], a[max] = a[max], a[right]
        left += 1
        right -= 1
    print(a)
a = [5, 1, 4, 2, 8]
sapxep(a)