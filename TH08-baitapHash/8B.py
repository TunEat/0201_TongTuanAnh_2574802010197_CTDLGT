#bai 8
# Hàm băm 1: lấy phần dư
def hash1(k, m):
    return k % m


# Hàm băm 2: nhân với 7 rồi lấy phần dư
def hash2(k, m):
    return (k * 7) % m


# Hàm tính Chi-square
def chi_square(keys, hash_func, m):

    # Tạo m bucket, ban đầu mỗi bucket có 0 phần tử
    buckets = [0] * m

    # Đếm số phần tử trong từng bucket
    for key in keys:

        # Tính bucket của khóa
        index = hash_func(key, m)

        # Tăng số phần tử trong bucket đó
        buckets[index] += 1

    # Số phần tử mong đợi ở mỗi bucket
    expected = len(keys) / m

    # Giá trị Chi-square
    chi = 0

    # Tính Chi-square
    for count in buckets:

        # Công thức Chi-square
        chi += (count - expected) ** 2 / expected

    # Trả về số phần tử trong các bucket và giá trị Chi-square
    return buckets, chi


# Danh sách khóa
keys = [10, 20, 30, 40, 50, 60, 70, 80]

# Số bucket
m = 7

# Tính kết quả cho hàm băm 1
bucket1, chi1 = chi_square(keys, hash1, m)

# Tính kết quả cho hàm băm 2
bucket2, chi2 = chi_square(keys, hash2, m)

# In kết quả của hàm băm 1
print("Hash 1:", bucket1)
print("Chi-square:", chi1)

print()

# In kết quả của hàm băm 2
print("Hash 2:", bucket2)
print("Chi-square:", chi2)

# So sánh hai hàm băm
if chi1 < chi2:
    print("\nHash 1 phân bố đều hơn")
elif chi2 < chi1:
    print("\nHash 2 phân bố đều hơn")
else:
    print("\nHai hàm băm có chất lượng phân bố như nhau")