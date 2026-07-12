#bai 3b
# Hàm băm Polynomial Rolling Hash
def polynomial_hash(s, p, m):
    h = 0
    n = len(s)

    # Duyệt từng ký tự trong chuỗi
    for i in range(n):

        # Cộng giá trị của từng ký tự vào hash
        h = (h + ord(s[i]) * (p ** (n - i - 1))) % m

    # Trả về giá trị hash
    return h
# Chuỗi cần băm
s = "abc"
# Cơ số và số nguyên tố
p = 31
m = 1000000007

# In giá trị hash
print("Hash =", polynomial_hash(s, p, m))
#p là cơ số (base) của hàm băm.
#Nó quyết định trọng số của từng ký tự trong chuỗi, giúp phân biệt vị trí của các ký tự.