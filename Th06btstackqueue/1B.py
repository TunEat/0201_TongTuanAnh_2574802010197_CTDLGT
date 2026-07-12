# Bài 1: Cài đặt hàng đợi cơ bản
# Queue hoạt động theo nguyên tắc FIFO (First In - First Out)
# Vào trước ra trước


class Queue:

    def __init__(self):
        self.queue = []  # Danh sách lưu các phần tử trong queue


    # Thêm phần tử vào cuối hàng đợi
    def enqueue(self, x):
        self.queue.append(x)
        print("Enqueue:", x)


    # Lấy phần tử đầu hàng đợi ra
    def dequeue(self):

        if self.isEmpty():
            print("Queue rỗng")
            return None

        return self.queue.pop(0)


    # Lấy phần tử đầu hàng đợi nhưng không xóa
    def front(self):

        if self.isEmpty():
            return None

        return self.queue[0]


    # Kiểm tra queue có rỗng không
    def isEmpty(self):

        return len(self.queue) == 0



q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Dequeue:", q.dequeue())
print("Front:", q.front())