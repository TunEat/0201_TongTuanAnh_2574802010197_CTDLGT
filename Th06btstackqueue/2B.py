# Bài 2: Cài đặt Circular Queue
# Dùng mảng cố định và chỉ số mod để quay vòng


class CircularQueue:

    def __init__(self, size):

        self.size = size       # Sức chứa tối đa
        self.queue = [None]*size

        self.front = 0         # Vị trí đầu queue
        self.rear = 0          # Vị trí thêm phần tử
        self.count = 0         # Số phần tử hiện tại



    # Thêm phần tử vào queue
    def enqueue(self, x):

        if self.count == self.size:
            print("Queue đầy")
            return


        self.queue[self.rear] = x

        # quay vòng chỉ số
        self.rear = (self.rear + 1) % self.size

        self.count += 1



    # Lấy phần tử ra khỏi queue
    def dequeue(self):

        if self.count == 0:
            print("Queue rỗng")
            return None


        x = self.queue[self.front]

        self.front = (self.front + 1) % self.size

        self.count -= 1

        return x



q = CircularQueue(4)


q.enqueue(1)
q.enqueue(2)
q.enqueue(3)


print(q.dequeue())
print(q.dequeue())