#bai 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Hàm tìm kiếm
def search(head, value):

    # Bắt đầu từ nút đầu
    current = head

    # Vị trí của nút
    index = 0

    # Duyệt danh sách
    while current is not None:

        # Nếu tìm thấy
        if current.data == value:
            return index

        # Sang nút tiếp theo
        current = current.next
        index += 1

    # Không tìm thấy
    return -1


# Tạo danh sách: 1 -> 2 -> 3 -> null
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Tìm giá trị 2
print(search(head, 2))