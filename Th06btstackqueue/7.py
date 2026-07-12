# Bài 7: Cài đặt MinStack
class MinStack:

    # Hàm khởi tạo Stack
    def __init__(self):
        self.stack = []       # Stack chính dùng để lưu tất cả phần tử
        self.min_stack = []   # Stack phụ dùng để lưu các giá trị nhỏ nhất


    # Hàm thêm phần tử vào Stack (Push)
    def push(self, x):

        self.stack.append(x)  # Thêm x vào stack chính

        # Nếu min_stack rỗng hoặc x nhỏ hơn / bằng giá trị nhỏ nhất hiện tại
        # thì thêm x vào min_stack
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)


    # Hàm lấy phần tử trên cùng ra khỏi Stack (Pop)
    def pop(self):

        x = self.stack.pop()  # Lấy và xóa phần tử trên cùng của stack chính

        # Nếu phần tử vừa lấy ra cũng là giá trị nhỏ nhất
        # thì xóa nó khỏi min_stack
        if x == self.min_stack[-1]:
            self.min_stack.pop()

        return x  # Trả về phần tử vừa lấy ra


    # Hàm lấy giá trị nhỏ nhất hiện tại trong Stack
    def getMin(self):

        return self.min_stack[-1]  # Phần tử cuối của min_stack là giá trị nhỏ nhất



# Tạo một MinStack mới
s = MinStack()


# Thêm các phần tử vào Stack
s.push(5)  # stack = [5], min_stack = [5]

s.push(3)  # stack = [5,3], min_stack = [5,3]

s.push(7)  # stack = [5,3,7], min_stack = [5,3]


# Lấy và in giá trị nhỏ nhất trong Stack
print("Min:", s.getMin())