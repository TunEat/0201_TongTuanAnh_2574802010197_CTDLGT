# Bảng băm với dò tuyến tính (Linear Probing)
DELETED = "DELETED"
class HashTableLinearProbing:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        """Thêm (key, value): nếu va chạm, dò tuyến tính i+1, i+2, ..."""
        index = self._hash(key)
        step = 0

        while step < self.size:
            current_index = (index + step) % self.size

            if self.table[current_index] is None or self.table[current_index] == DELETED:
                self.table[current_index] = (key, value)
                return

            step += 1

    def get(self, key):
        """Tìm key: dò tuyến tính từ vị trí hash ban đầu"""
        index = self._hash(key)
        step = 0

        while step < self.size:
            current_index = (index + step) % self.size

            if self.table[current_index] is None:
                return None

            if self.table[current_index] != DELETED:
                k, v = self.table[current_index]
                if k == key:
                    return v

            step += 1

        return None

    def remove(self, key):
        """Xóa key: đánh dấu ô là DELETED"""
        index = self._hash(key)
        step = 0

        while step < self.size:
            current_index = (index + step) % self.size

            if self.table[current_index] is None:
                return

            if self.table[current_index] != DELETED:
                k, v = self.table[current_index]
                if k == key:
                    self.table[current_index] = DELETED
                    return

            step += 1


# Test
ht = HashTableLinearProbing(5)
ht.put("a", 1)
ht.put("b", 2)
print(ht.get("a"))  # 1
ht.remove("a")
print(ht.get("a"))  # None

