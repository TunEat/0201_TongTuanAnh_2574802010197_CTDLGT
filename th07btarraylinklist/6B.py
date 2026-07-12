#bai 6B
class Node:
    def __init__(self, data):
        self.data = data      # Giá trị nút
        self.next = None      # Nút tiếp theo

# Hàm đảo ngược bằng 3 con trỏ
def reverse_iterative(head):

    # 3 con trỏ
    prev = None
    cur = head

    while cur:

        # Lưu nút kế tiếp
        next = cur.next

        # Đảo chiều liên kết
        cur.next = prev

        # Di chuyển các con trỏ
        prev = cur
        cur = next

    # prev là head mới
    return prev


# In danh sách
def printList(head):

    while head:
        print(head.data, end=" -> ")
        head = head.next

    print("null")


# Tạo danh sách 1 -> 2 -> 3 -> null
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Đảo ngược
head = reverse_iterative(head)

# In kết quả
printList(head)