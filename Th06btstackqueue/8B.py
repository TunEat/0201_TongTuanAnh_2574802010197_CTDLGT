# Bài 8: Deque
# Cho phép thêm/xóa ở cả hai đầu


from collections import deque


dq = deque()


# Thêm vào đầu Queue
dq.appendleft(1)


# Thêm vào cuối Queue
dq.append(2)


print(dq)


# Xóa ở đầu
print("Pop Front:", dq.popleft())


# Xóa ở cuối
print("Pop Back:", dq.pop())