#bai 4
MAX_SIZE = 3  # Giới hạn số lượng phần tử tối đa của stack

stack = []  # Tạo một stack rỗng


# Hàm thêm phần tử vào stack (Push)
def push(x):
    # Kiểm tra nếu stack đã đầy
    if len(stack) == MAX_SIZE:
        print("Lỗi Overflow")  # Không thể thêm phần tử vì stack đã đầy
    else:
        stack.append(x)  # Thêm phần tử x vào đỉnh stack
        print("Push:", x)  # In ra phần tử vừa thêm


# Hàm lấy phần tử ra khỏi stack (Pop)
def pop():
    # Kiểm tra nếu stack đang rỗng
    if len(stack) == 0:
        print("Lỗi Underflow")  # Không thể lấy phần tử vì stack rỗng
    else:
        print("Pop:", stack.pop())  # Lấy và xóa phần tử trên cùng của stack


# Thêm các phần tử vào stack
push(1)  # stack = [1]
push(2)  # stack = [1, 2]
push(3)  # stack = [1, 2, 3]


# Thử thêm phần tử khi stack đã đầy
push(4)  # Xảy ra lỗi Overflow vì MAX_SIZE = 3


# Lấy các phần tử ra khỏi stack
pop()  # Lấy 3, stack = [1, 2]
pop()  # Lấy 2, stack = [1]
pop()  # Lấy 1, stack = []


# Thử lấy phần tử khi stack đã rỗng
pop()  # Xảy ra lỗi Underflow