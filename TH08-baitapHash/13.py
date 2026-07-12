#bai 13 
def longest_consecutive(nums):
    # Chuyển mảng thành Hash Set
    s = set(nums)

    # Lưu độ dài lớn nhất
    longest = 0

    # Lưu số bắt đầu của dãy dài nhất
    start = 0

    # Duyệt từng phần tử
    for x in s:

        # Nếu x là đầu dãy
        if x - 1 not in s:

            length = 1

            # Đếm các số liên tiếp
            while x + length in s:
                length += 1

            # Cập nhật dãy dài nhất
            if length > longest:
                longest = length
                start = x

    # In dãy liên tiếp dài nhất
    for i in range(longest):
        print(start + i, end=" ")


# Mảng đầu vào
a = [100, 4, 200, 1, 3, 2]

# Gọi hàm
longest_consecutive(a)