#bai 11
# Hàm đảo một đoạn của mảng
def reverse(arr, left, right):

    # Đổi chỗ hai đầu rồi tiến vào giữa
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


# Hàm xoay mảng
def rotate(arr, k):

    # Độ dài mảng
    n = len(arr)

    # Nếu k lớn hơn n
    k = k % n

    # Đảo toàn bộ mảng
    reverse(arr, 0, n - 1)

    # Đảo k phần tử đầu
    reverse(arr, 0, k - 1)

    # Đảo các phần tử còn lại
    reverse(arr, k, n - 1)


# Mảng ban đầu
a = [1, 2, 3, 4, 5]

# Số vị trí cần xoay
k = 2

# Xoay mảng
rotate(a, k)

# In kết quả
print(a)