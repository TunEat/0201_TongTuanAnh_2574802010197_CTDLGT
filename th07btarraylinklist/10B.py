#bai 10b 
class Node:
    def __init__(self, data):
        self.data = data      # Giá trị nút
        self.next = None      # Nút kế tiếp


# Xóa nút thứ k từ cuối
def remove_kth(head, k):

    # Nút giả
    dummy = Node(0)
    dummy.next = head

    # Hai con trỏ
    slow = fast = dummy

    # Cho fast đi trước k bước
    for _ in range(k):
        fast = fast.next

    # Di chuyển cùng nhau
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Xóa nút cần tìm
    slow.next = slow.next.next

    return dummy.next


# In danh sách
def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("null")


# Tạo danh sách 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Xóa nút thứ 2 từ cuối
head = remove_kth(head, 2)

# In kết quả
printList(head)