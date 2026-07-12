#bai 7b
class Node:
    def __init__(self, data):
        self.data = data      # Giá trị nút
        self.next = None      # Nút tiếp theo
# Hàm tìm nút giữa
def find_middle(head):

    # Con trỏ chậm đi 1 bước
    slow = head

    # Con trỏ nhanh đi 2 bước
    fast = head

    # Duyệt danh sách
    while fast and fast.next:

        # Slow đi 1 nút
        slow = slow.next

        # Fast đi 2 nút
        fast = fast.next.next

    # Khi fast đến cuối, slow ở giữa
    return slow.data


# Tạo danh sách: 1 -> 2 -> 3 -> 4 -> 5 -> null
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# In nút giữa
print("Nút giữa:", find_middle(head))