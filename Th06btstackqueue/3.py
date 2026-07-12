# Bài 3
stack = []  # Tạo một ngăn xếp rỗng để lưu các phần tử
# Danh sách các thao tác gồm:
# ("push", giá trị): thêm phần tử vào stack
# ("pop", None): lấy phần tử trên cùng ra khỏi stack
operations = [
    ("push", 5),
    ("push", 7),
    ("pop", None)
]


# Duyệt lần lượt từng thao tác trong danh sách operations
for op, value in operations:

    # Nếu thao tác là push
    if op == "push":
        stack.append(value)  # Thêm giá trị vào cuối stack
        print("Push:", value)  # In giá trị vừa thêm vào

    # Nếu thao tác là pop
    elif op == "pop":
        # Kiểm tra stack có phần tử hay không
        if len(stack) > 0:
            x = stack.pop()  # Lấy và xóa phần tử trên cùng của stack
            print("Pop:", x)  # In giá trị vừa lấy ra
        else:
            print("Stack rỗng")  # Thông báo nếu stack không có phần tử


# In trạng thái cuối cùng của stack sau khi thực hiện các thao tác
print("Stack cuối cùng:", stack)