from collections import deque

A = [4, 2, 12, 11, -5, 8, 1, 5, 6]
k = 3

dq = deque()
result = []

for i in range(len(A)):

    # Xóa phần tử nằm ngoài cửa sổ
    while dq and dq[0] <= i - k:
        dq.popleft()

    # Xóa các phần tử lớn hơn phần tử hiện tại
    while dq and A[dq[-1]] > A[i]:
        dq.pop()

    # Thêm chỉ số hiện tại
    dq.append(i)

    # Khi đủ k phần tử
    if i >= k - 1:
        result.append(A[dq[0]])

print(result)
#Thuật toán luôn so sánh phần tử hiện tại với phần
#tử ở cuối Deque để loại bỏ các phần tử lớn hơn 
#vì chúng không thể trở thành giá trị nhỏ nhất trong 
#các cửa sổ tiếp theo. Đồng thời, thuật toán xóa các phần tử đã ra khỏi cửa sổ.
#Nhờ đó, đầu Deque luôn chứa chỉ số của phần tử nhỏ nhất trong cửa sổ hiện tại,
#giúp tìm giá trị nhỏ nhất của mỗi cửa sổ với độ phức tạp O(N).