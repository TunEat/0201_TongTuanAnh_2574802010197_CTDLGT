# Bài 6: Queue sử dụng 2 Stack
# Dùng nguyên lý:
# Stack LIFO -> mô phỏng Queue FIFO


class QueueUsingStack:


    def __init__(self):

        self.in_stack = []   # Stack chứa dữ liệu thêm vào
        self.out_stack = []  # Stack dùng để lấy dữ liệu ra



    # Thêm phần tử vào Queue
    def enqueue(self,x):

        self.in_stack.append(x)



    # Lấy phần tử đầu Queue
    def dequeue(self):

        # Nếu out_stack rỗng thì chuyển dữ liệu từ in sang out
        if not self.out_stack:

            while self.in_stack:

                self.out_stack.append(
                    self.in_stack.pop()
                )


        if not self.out_stack:

            return None


        return self.out_stack.pop()



q = QueueUsingStack()


q.enqueue(1)
q.enqueue(2)
q.enqueue(3)


print(q.dequeue())
print(q.dequeue())