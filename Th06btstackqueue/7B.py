# Bài 7: Đảo ngược Queue bằng Stack
# Dùng Stack để đảo thứ tự phần tử


from collections import deque


def reverse_queue(queue):

    stack = []  # Stack phụ


    # Đưa tất cả phần tử Queue vào Stack
    while queue:

        stack.append(queue.popleft())


    # Lấy từ Stack đưa lại Queue
    while stack:

        queue.append(stack.pop())



q = deque([1,2,3])


reverse_queue(q)


print(q)