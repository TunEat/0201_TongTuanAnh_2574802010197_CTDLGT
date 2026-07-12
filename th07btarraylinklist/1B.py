#bai 1b
class Node:
    def __init__(self, data):
        self.data = data      # Giá trị nút
        self.next = None      # Nút tiếp theo
# Tạo danh sách liên kết
class LinkedList:
    def __init__(self):
        self.head = None      # Nút đầu

    # Thêm vào đầu
    def pushFront(self, data):
        node = Node(data)     # Tạo nút mới
        node.next = self.head # Nối với danh sách cũ
        self.head = node      # Cập nhật đầu

    # Thêm vào cuối
    def pushBack(self, data):
        node = Node(data)     # Tạo nút mới

        if self.head is None:
            self.head = node
            return

        cur = self.head       # Duyệt từ đầu
        while cur.next:
            cur = cur.next

        cur.next = node       # Nối vào cuối


    # In danh sách
    def printList(self):
        cur = self.head

        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next

        print("null")

# Test
lst = LinkedList()

lst.pushFront(2)   # Thêm đầu 2
lst.pushBack(5)    # Thêm cuối 5

lst.printList()    # In danh sách