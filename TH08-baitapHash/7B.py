#bai 7
# Hằng số dùng để kết hợp hash
C = 31

# Hàm băm cho cặp
def hash_pair(a, b):

    # Tính hash của từng phần tử
    hash_a = hash(a)
    hash_b = hash(b)

    # Kết hợp hai hash bằng phép nhân và XOR
    return (hash_a * C) ^ hash_b

# Cặp cần băm
a = 5
b = 10

# In giá trị hash
print("Hash của (5,10):", hash_pair(a, b))