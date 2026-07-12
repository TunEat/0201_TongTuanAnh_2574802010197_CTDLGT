#bai 12
# Bài 12: Đếm số đoạn con có tổng bằng k

def subarray_sum(nums, k):
    # Tổng tiền tố
    prefix = 0

    # Đếm số đoạn con có tổng bằng k
    count = 0

    # Hash Map lưu: tổng tiền tố -> số lần xuất hiện
    # Ban đầu tổng = 0 xuất hiện 1 lần
    hash_map = {0: 1}

    # Duyệt từng phần tử trong mảng
    for x in nums:

        # Cập nhật tổng tiền tố
        prefix += x

        # Nếu tồn tại tổng tiền tố = prefix - k
        # thì đã tìm được đoạn con có tổng bằng k
        if prefix - k in hash_map:
            count += hash_map[prefix - k]

        # Cập nhật số lần xuất hiện của tổng tiền tố
        hash_map[prefix] = hash_map.get(prefix, 0) + 1

    # Trả về số đoạn con
    return count


# Mảng đầu vào
a = [1, 1, 1]

# Giá trị cần tìm
k = 2

# In kết quả
print(subarray_sum(a, k), "đoạn")