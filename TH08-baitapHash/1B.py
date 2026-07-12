# baii 1B

# Hàm băm
def hash_mod(k, m):
    # Trả về chỉ số bucket
    return k % m

# Danh sách các khóa
keys = [37, 25, 18, 42, 56]

# Số bucket
m = 10
# Tính bucket của từng khóa
for k in keys:
    print(k, "-> Bucket", hash_mod(k, m))