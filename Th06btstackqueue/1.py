#phần A 
#bài 1 cài đặt ngăn xếp mảng
class Stack:
    def __init__(self):
        self.stack = []
    # Thêm phần tử vào đỉnh stack
    def push(self, x):
        self.stack.append(x)

    # Lấy và xóa phần tử trên cùng
    def pop(self):
        if self.isEmpty():
            print("Stack rỗng!")
            return None
        return self.stack.pop()
    # Xem phần tử trên cùng
    def top(self):
        if self.isEmpty():
            print("Stack rỗng!")
            return None
        return self.stack[-1]
    # Kiểm tra stack rỗng
    def isEmpty(self):
        return len(self.stack) == 0
    # In stack
    def display(self):
        print(self.stack)

# Chương trình chính
s = Stack()
s.push(1)
s.push(2)
s.push(3)

print("Stack:")
s.display()
print("Top:", s.top())
print("Pop:", s.pop())
print("Sau khi pop:")
s.display()
print("Stack rỗng?", s.isEmpty())