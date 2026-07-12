#bài 14 slection sort trên danh sách liên kết
# Bài 14: Selection sort trên danh sách liên kết đơn

# Tạo nút
class Node:
    def __init__(self, data):
        self.data = data      # Giá trị nút
        self.next = None      # Nút tiếp theo


# Selection sort trên linked list
def selection_sort(head):

    # Danh sách kết quả đã sắp xếp
    sorted_head = None
    sorted_tail = None

    # Duyệt đến khi danh sách cũ rỗng
    while head:

        # Tìm nút nhỏ nhất
        minNode = head
        minPrev = None

        prev = head
        cur = head.next

        while cur:

            if cur.data < minNode.data:
                minNode = cur
                minPrev = prev

            prev = cur
            cur = cur.next

        # Xóa nút nhỏ nhất khỏi danh sách cũ
        if minPrev:
            minPrev.next = minNode.next
        else:
            head = minNode.next

        # Tách nút nhỏ nhất
        minNode.next = None

        # Nối vào danh sách kết quả
        if sorted_head is None:
            sorted_head = minNode
            sorted_tail = minNode
        else:
            sorted_tail.next = minNode
            sorted_tail = minNode

    return sorted_head


# In danh sách
def printList(head):

    while head:
        print(head.data, end=" -> ")
        head = head.next

    print("null")


# Tạo danh sách: 3 -> 1 -> 2 -> null
head = Node(3)
head.next = Node(1)
head.next.next = Node(2)

# Sắp xếp
head = selection_sort(head)

# In kết quả
printList(head)