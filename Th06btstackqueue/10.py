# Bài 10: Cài đặt Stack bằng Queue
# Dùng Queue (FIFO) để mô phỏng Stack (LIFO)
from collections import deque  # Import deque để sử dụng Queue
class StackUsingQueue:


    # Hàm khởi tạo
    def __init__(self):

        self.q1 = deque()  # Queue chính dùng để lưu dữ liệu của Stack
        self.q2 = deque()  # Queue phụ dùng khi thêm phần tử mới



    # Hàm thêm phần tử vào Stack (Push)
    def push(self, x):

        # Đưa phần tử mới vào q2 trước
        # Vì phần tử mới cần nằm ở đầu để được lấy ra trước
        self.q2.append(x)


        # Chuyển toàn bộ phần tử từ q1 sang q2
        # để đưa phần tử mới lên đầu Queue
        while self.q1:
            self.q2.append(self.q1.popleft())


        # Đổi vai trò của q1 và q2
        # q1 luôn là Queue chính chứa Stack hiện tại
        self.q1, self.q2 = self.q2, self.q1



    # Hàm lấy phần tử ra khỏi Stack (Pop)
    def pop(self):

        # Nếu q1 rỗng thì Stack không có phần tử
        if not self.q1:
            return None


        # Lấy phần tử đầu Queue
        # Do đã sắp xếp lại nên đây chính là phần tử trên cùng của Stack
        return self.q1.popleft()



# Tạo một Stack mới sử dụng Queue
stack = StackUsingQueue()


# Thêm các phần tử vào Stack
stack.push(1)  # Stack: [1]

stack.push(2)  # Stack: [2,1]

stack.push(3)  # Stack: [3,2,1]


# Lấy phần tử ra khỏi Stack
print(stack.pop())  # Lấy 3

print(stack.pop())  # Lấy 2