#bai 4b
# Bài 4: Kiểm tra Queue rỗng hoặc đầy


class QueueLimit:


    def __init__(self, size):

        self.size = size

        self.queue = []



    # Thêm phần tử
    def enqueue(self,x):

        # Kiểm tra queue đầy
        if len(self.queue) == self.size:

            print("Lỗi: Queue đầy")

        else:

            self.queue.append(x)

            print("Enqueue:",x)



    # Lấy phần tử
    def dequeue(self):

        # Kiểm tra queue rỗng
        if len(self.queue)==0:

            print("Lỗi: Queue rỗng")

        else:

            print("Dequeue:",self.queue.pop(0))



q = QueueLimit(3)


q.enqueue(1)
q.enqueue(2)
q.enqueue(3)


# Queue đầy
q.enqueue(4)


q.dequeue()
q.dequeue()
q.dequeue()


# Queue rỗng
q.dequeue()