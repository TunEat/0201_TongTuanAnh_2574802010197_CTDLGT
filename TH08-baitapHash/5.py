#bai 5
# Bài 5: Nhóm các từ theo chữ cái đầu

def a(words):
    # Tạo Dictionary rỗng để lưu kết quả
    groups = {}

    # Duyệt từng từ trong danh sách
    for word in words:

        # Lấy chữ cái đầu của từ làm khóa
        key = word[0]

        # Nếu khóa chưa có trong Dictionary
        if key not in groups:
            # Tạo một danh sách rỗng cho khóa đó
            groups[key] = []

        # Thêm từ vào danh sách của khóa tương ứng
        groups[key].append(word)

    # Trả về kết quả sau khi nhóm
    return groups


# Danh sách các từ
words = ["apple", "ant", "banana", "ball", "cat"]

# Gọi hàm và in kết quả
print(a(words))
# Kết quả:
# {
#   'a': ['apple', 'ant'],
#   'b': ['banana', 'ball'],
#   'c': ['cat']
# }