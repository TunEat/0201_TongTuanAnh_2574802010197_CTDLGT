class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Tìm nút bắt đầu chu trình
def detectCycle(head):
    slow = head
    fast = head

    # Giai đoạn 1: Tìm điểm gặp nhau
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None    # Không có chu trình

    # Giai đoạn 2: Tìm nút bắt đầu chu trình
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# Tạo danh sách liên kết
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Tạo chu trình: 5 -> 3
head.next.next.next.next.next = head.next.next

start = detectCycle(head)

if start:
    print("Nút bắt đầu chu trình:", start.data)
else:
    print("Không có chu trình")

#Kết luận giai đoạn 2: Sau khi phát hiện chu trình, 
# đưa một con trỏ về Head và giữ con trỏ còn lại tại điểm gặp nhau. 
# Cho cả hai cùng di chuyển 1 bước mỗi lần, chúng sẽ gặp nhau đúng tại nút bắt đầu của chu trình. 
# Điều này đúng vì khoảng cách từ Head đến nút bắt đầu chu trình bằng khoảng cách từ điểm gặp 
# nhau đến nút bắt đầu chu trình (theo quan hệ toán học của thuật toán Floyd).