class bangbam:
    def __init__(self, size):
        # Tạo bảng băm có 'size' bucket (mỗi bucket là một danh sách rỗng)
        self.table = [[] for _ in range(size)]

    def put(self, key, value):
        # Tính vị trí lưu bằng hàm băm
        index = hash(key) % len(self.table)
        # Thêm cặp (key, value) vào bucket
        self.table[index].append((key, value))

    def get(self, key):
        # Tính vị trí của key cần tìm
        index = hash(key) % len(self.table)
        #duyet tung phan tu trong bucket
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        # Tính vị trí của key cần xóa
        index = hash(key) % len(self.table)

        # enumerate() trả về cả chỉ số (i) và giá trị (k, v)
        for i, (k, v) in enumerate(self.table[index]):

            # Nếu tìm thấy key
            if k == key:
                # Xóa phần tử khỏi bucket
                del self.table[index][i]
                return

# Tạo bảng băm gồm 5 buckets
ht = bangbam(5)
ht.put("a", 1)#them6 du lieu vao
ht.put("b", 2)
print(ht.get("a"))  # lay gia tri key la a
ht.remove("a")#xoa
print(ht.get("a")) #ket qua ra None la xoa roi
