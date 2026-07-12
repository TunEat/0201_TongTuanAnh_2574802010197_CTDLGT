# Bài 5
stack = [1, 2, 3, 4]  # Tạo stack ban đầu gồm các phần tử
temp = []  # Tạo stack phụ để lưu tạm các phần tử đã lấy ra

count = 0  # Biến đếm số lượng phần tử trong stack


# Lấy từng phần tử ra khỏi stack để duyệt
# Vì Stack hoạt động theo nguyên tắc LIFO nên phần tử cuối được lấy trước
while stack:
    x = stack.pop()  # Lấy phần tử trên cùng của stack
    print(x)  # In phần tử vừa lấy ra

    count += 1  # Tăng số lượng phần tử đã duyệt lên 1
    temp.append(x)  # Lưu phần tử vào stack phụ để khôi phục lại


# Khôi phục lại stack ban đầu
# Lấy phần tử từ temp và đưa ngược trở lại stack
while temp:
    stack.append(temp.pop())


# In số lượng phần tử đã duyệt
print("Số phần tử:", count)

# In trạng thái stack sau khi khôi phục
print("Stack sau khi duyệt:", stack)