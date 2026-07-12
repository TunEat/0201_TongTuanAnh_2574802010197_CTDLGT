#Bai 6
def check_parentheses(s):

    stack = []  # Tạo stack rỗng để lưu các dấu ngoặc mở

    # Tạo bảng ánh xạ giữa dấu ngoặc đóng và dấu ngoặc mở tương ứng
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }


    # Duyệt từng ký tự trong chuỗi s
    for char in s:

        # Nếu gặp dấu ngoặc mở thì đưa vào stack
        if char in "([{":
            stack.append(char)


        # Nếu gặp dấu ngoặc đóng
        elif char in ")]}":

            # Kiểm tra stack có rỗng không
            # Nếu rỗng nghĩa là không có dấu ngoặc mở để ghép
            if len(stack) == 0:
                return False

            # Lấy dấu ngoặc mở trên cùng ra khỏi stack
            # Nếu không khớp với dấu ngoặc đóng hiện tại thì sai
            if stack.pop() != pairs[char]:
                return False


    # Sau khi duyệt hết chuỗi:
    # Stack rỗng nghĩa là tất cả dấu ngoặc đã được đóng đúng
    # Stack còn phần tử nghĩa là còn dấu ngoặc mở chưa đóng
    return len(stack) == 0



s = "{[()]}"  # Chuỗi cần kiểm tra


# Gọi hàm kiểm tra và in kết quả
print(check_parentheses(s))