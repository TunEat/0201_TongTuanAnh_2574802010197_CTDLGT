#bai 10
import math
# Hàm băm theo phương pháp nhân
def multiplication_hash(k, m):

    # Tỉ lệ vàng
    A = 0.6180339887

    # Lấy phần thập phân của k*A
    fraction = (k * A) % 1

    # Tính bucket
    return math.floor(m * fraction)


# Hàm băm theo phương pháp chia
def division_hash(k, m):
    return k % m
# Danh sách khóa
keys = [10, 20, 30, 40, 50]

# Số bucket
m = 10

print("Phương pháp nhân:")
for key in keys:
    print(key, "-> Bucket", multiplication_hash(key, m))

print()

print("Phương pháp chia:")
for key in keys:
    print(key, "-> Bucket", division_hash(key, m))