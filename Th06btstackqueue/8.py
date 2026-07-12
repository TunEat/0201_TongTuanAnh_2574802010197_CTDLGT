# Bài 8: Tính biểu thức RPN (Reverse Polish Notation)
# RPN là dạng biểu thức hậu tố, trong đó toán tử đứng sau các toán hạng
# Ví dụ: 3 4 + nghĩa là 3 + 4


def evaluate(expression):

    stack = []  # Tạo stack rỗng để lưu các số

    # Tách biểu thức thành từng phần tử riêng biệt
    # Ví dụ: "3 4 + 2 *" -> ["3", "4", "+", "2", "*"]
    tokens = expression.split()


    # Duyệt từng phần tử trong biểu thức
    for token in tokens:

        # Nếu token là số
        if token.isdigit():

            # Đưa số vào stack
            stack.append(int(token))


        # Nếu token là toán tử
        else:

            # Lấy 2 số trên cùng của stack ra
            # Số lấy ra trước là toán hạng bên phải
            # Số lấy ra sau là toán hạng bên trái
            b = stack.pop()
            a = stack.pop()


            # Thực hiện phép tính tương ứng
            if token == "+":
                stack.append(a + b)  # Cộng 2 số

            elif token == "-":
                stack.append(a - b)  # Trừ a cho b

            elif token == "*":
                stack.append(a * b)  # Nhân 2 số

            elif token == "/":
                stack.append(a / b)  # Chia a cho b


    # Sau khi tính xong, stack chỉ còn lại một kết quả
    return stack.pop()



# Biểu thức RPN cần tính
exp = "3 4 + 2 *"


# Gọi hàm và in kết quả
print(evaluate(exp))