#bai 2b
# Bài 2: Hàm băm cho chuỗi

# Hàm băm
def hash_string(s, m):
    total = 0

    # Tính tổng mã ASCII của các ký tự
    for ch in s:
        total += ord(ch)

    # Trả về chỉ số bucket
    return total % m


# Số bucket
m = 10

# Hai chuỗi cần kiểm tra
s1 = "abc"
s2 = "cba"

# In giá trị hash
print(s1, "->", hash_string(s1, m))
print(s2, "->", hash_string(s2, m))