#bai 11
# Bài 11: Cài đặt HashSet

class HashSet:
    def __init__(self):
        # Tạo Dictionary rỗng để lưu các phần tử
        self.table = {}

    # Thêm phần tử vào HashSet
    def add(self, x):
        # Nếu x đã tồn tại thì chỉ cập nhật lại, không tạo phần tử trùng
        self.table[x] = True

    # Kiểm tra phần tử có trong HashSet hay không
    def contains(self, x):
        return x in self.table

    # Xóa phần tử khỏi HashSet
    def remove(self, x):
        if x in self.table:
            del self.table[x]

    # Hiển thị HashSet
    def display(self):
        # Lấy các khóa (keys) của Dictionary và chuyển thành set
        return set(self.table.keys())


# Tạo một HashSet
s = HashSet()

# Thêm các phần tử
s.add(1)
s.add(1)      # Không thêm vì 1 đã tồn tại
s.add(2)

# In HashSet
print(s.display())
# Kết quả: {1, 2}

# Kiểm tra phần tử
print(s.contains(1))
# Kết quả: True

print(s.contains(3))
# Kết quả: False

# Xóa phần tử 1
s.remove(1)

# In HashSet sau khi xóa
print(s.display())
# Kết quả: {2}