def reverse_string(s):
    stack = []  # Tạo một ngăn xếp (stack) rỗng để lưu các ký tự

    # Đưa từng ký tự trong chuỗi s vào stack
    # Ký tự được thêm vào cuối stack theo thứ tự ban đầu
    for char in s:
        stack.append(char)

    result = ""  # Tạo chuỗi kết quả rỗng để lưu chuỗi đảo ngược

    # Lấy từng ký tự ra khỏi stack
    # Stack hoạt động theo nguyên tắc LIFO (Last In - First Out)
    # Ký tự vào sau sẽ được lấy ra trước
    while stack:
        result += stack.pop()

    return result  # Trả về chuỗi sau khi đã đảo ngược


s = "abc"  # Chuỗi ban đầu

print(reverse_string(s))  # In ra kết quả: cba