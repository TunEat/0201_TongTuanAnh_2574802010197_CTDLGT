class HashTable:
    def __init__(self):
        # Tạo một Dictionary rỗng để lưu tần suất
        self.table = {}

    def put(self, key):
        # Nếu key đã có thì tăng lên 1
        # Nếu chưa có thì gán giá trị ban đầu là 0 rồi cộng 1
        self.table[key] = self.table.get(key, 0) + 1

    def get_result(self):
        # Trả về bảng tần suất
        return self.table

def count_frequency(arr):
    # Tạo một đối tượng HashTable
    ht = HashTable()

    # Duyệt từng phần tử trong mảng
    for item in arr:
        # Cập nhật số lần xuất hiện của phần tử
        ht.put(item)

    # Trả về kết quả
    return ht.get_result()

# Mảng cần đếm tần suất
arr = ['a', 'b', 'a', 'c', 'a']

# Gọi hàm và in kết quả
print(count_frequency(arr))

# Kết quả:
# {'a': 3, 'b': 1, 'c': 1}