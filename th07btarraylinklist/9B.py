#bai 9b
class Node:
    def __init__(self, data):
        self.data = data      # Giá trị nút
        self.next = None      # Nút tiếp theo
# Hàm trộn hai danh sách
def merge(head1, head2):

    # Tạo nút giả để dễ nối
    dummy = Node(0)
    # Con trỏ kết quả
    cur = dummy
    # Duyệt khi cả hai danh sách còn phần tử
    while head1 and head2:

        # Nếu nút bên 1 nhỏ hơn
        if head1.data <= head2.data:

            # Nối nút của danh sách 1 vào kết quả
            cur.next = head1

            # Di chuyển danh sách 1
            head1 = head1.next
        else:
            # Nối nút của danh sách 2 vào kết quả
            cur.next = head2
            # Di chuyển danh sách 2
            head2 = head2.next
        # Di chuyển con trỏ kết quả
        cur = cur.next
    # Nối phần còn lại của danh sách 1
    if head1:
        cur.next = head1

    # Nối phần còn lại của danh sách 2
    if head2:
        cur.next = head2
    # Trả về đầu danh sách mới
    return dummy.next
# In danh sách
def printList(head):

    while head:
        print(head.data, end=" -> ")
        head = head.next

    print("null")
# Tạo danh sách 1: 1 -> 3 -> 5
a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

# Tạo danh sách 2: 2 -> 4
b = Node(2)
b.next = Node(4)

# Trộn hai danh sách
head = merge(a, b)

# In kết quả
printList(head)