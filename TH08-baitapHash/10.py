#bai 10  d
# Bài 10: Tìm ký tự đầu tiên không lặp

def first_unique(s):
    # Tạo Dictionary để lưu số lần xuất hiện của mỗi ký tự
    count = {}

    # Duyệt chuỗi và đếm số lần xuất hiện của từng ký tự
    for ch in s:
        # Nếu ký tự đã có thì tăng lên 1
        # Nếu chưa có thì mặc định là 0 rồi cộng 1
        count[ch] = count.get(ch, 0) + 1

    # Duyệt lại chuỗi theo đúng thứ tự ban đầu
    for ch in s:

        # Nếu ký tự chỉ xuất hiện đúng 1 lần
        if count[ch] == 1:

            # Trả về ký tự đầu tiên không lặp
            return ch

    # Nếu không có ký tự nào xuất hiện đúng 1 lần
    return None


# Chuỗi cần kiểm tra
s = "leetcode"

# Gọi hàm và in kết quả
print(first_unique(s))

# Kết quả:
# l