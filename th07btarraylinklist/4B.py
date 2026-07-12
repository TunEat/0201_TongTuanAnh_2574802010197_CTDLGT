#bai 4
class Node:
    def __init__(self, data):
        self.data = data      # Giá trị nút
        self.next = None      # Nút tiếp theo


# Hàm chèn sau một nút
def insert_after(node, value):

    # Tạo nút mới
    newNode = Node(value)

    # Nút mới trỏ đến nút sau node hiện tại
    newNode.next = node.next

    # Node hiện tại trỏ đến nút mới
    node.next = newNode


# Hàm in danh sách
def printList(head):

    cur = head

    while cur:
        print(cur.data, end=" -> ")
        cur = cur.next

    print("null")


# Tạo danh sách: 1 -> 3 -> null
head = Node(1)
head.next = Node(3)

# Chèn 2 sau nút 1
insert_after(head, 2)

# In kết quả
printList(head)