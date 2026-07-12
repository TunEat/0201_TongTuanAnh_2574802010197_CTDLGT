#bai 5b
class Node:
    def __init__(self, data):
        self.data = data      # Giá trị nút
        self.next = None      # Nút tiếp theo


# Hàm xóa nút theo giá trị
def delete_value(head, x):

    # Nếu nút đầu có giá trị cần xóa
    if head and head.data == x:
        return head.next

    # Duyệt danh sách
    cur = head

    while cur.next:

        # Nếu nút kế tiếp có giá trị x
        if cur.next.data == x:

            # Bỏ qua nút cần xóa
            cur.next = cur.next.next
            break

        # Sang nút tiếp theo
        cur = cur.next

    return head


# Hàm in danh sách
def printList(head):

    while head:
        print(head.data, end=" -> ")
        head = head.next

    print("null")


# Tạo danh sách: 1 -> 2 -> 3 -> 2 -> null
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)

# Xóa nút có giá trị 2 đầu tiên
head = delete_value(head, 2)

# In kết quả
printList(head)