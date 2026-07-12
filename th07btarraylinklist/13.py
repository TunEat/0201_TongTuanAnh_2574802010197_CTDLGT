#bai 13
# Hàm gộp các khoảng
def merge_intervals(intervals):

    # Sắp xếp theo giá trị start
    intervals.sort(key=lambda x: x[0])

    # Danh sách kết quả
    result = []

    # Duyệt từng khoảng
    for interval in intervals:

        # Nếu result rỗng hoặc không giao nhau
        if not result or result[-1][1] < interval[0]:

            # Thêm khoảng mới vào kết quả
            result.append(interval)

        else:

            # Gộp hai khoảng bằng cách cập nhật end lớn hơn
            result[-1][1] = max(result[-1][1], interval[1])

    # Trả về danh sách sau khi gộp
    return result


# Danh sách các khoảng
intervals = [[1, 3], [2, 6], [8, 10]]

# In kết quả
print(merge_intervals(intervals))