#bai 9 
import random
# Số bucket
m = 10

# Số nguyên tố lớn
p = 101

# Chọn ngẫu nhiên a và b
a = random.randint(1, p - 1)
b = random.randint(0, p - 1)

# Hàm băm phổ quát
def universal_hash(k):
    return ((a * k + b) % p) % m

# Danh sách khóa
keys = [10, 20, 30, 40, 50]

# In giá trị a và b
print("a =", a)
print("b =", b)

# Tính bucket của từng khóa
for key in keys:
    print(key, "-> Bucket", universal_hash(key))