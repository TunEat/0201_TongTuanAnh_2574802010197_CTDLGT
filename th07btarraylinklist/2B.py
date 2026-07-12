#bai 2b
class Node:
    def __init__(self, data):
        self.data = data      # Giá trị nút
        self.next = None      # Nút tiếp theo


# Hàm duyệt và đếm số nút
def print_length(head):

    cur = head       # Bắt đầu từ nút đầu
    count = 0        # Biến đếm số nút

    while cur:

        print(cur.data, end=" -> ")  # In giá trị nút
        count += 1                   # Tăng số lượng nút
        cur = cur.next               # Sang nút tiếp theo

    print("null")
    print("Độ dài:", count)


# Tạo danh sách: 1 -> 2 -> 3 -> null
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Duyệt và tính độ dài
print_length(head)