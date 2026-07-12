#bai 10 trong hai ds sap xep
# Hàm trộn hai danh sách
def merge_sorted(a, b):

    # Danh sách kết quả
    result = []

    # Hai con trỏ của hai danh sách
    i = 0
    j = 0

    # Duyệt khi cả hai danh sách còn phần tử
    while i < len(a) and j < len(b):

        # Nếu phần tử của a nhỏ hơn hoặc bằng b
        if a[i] <= b[j]:

            # Thêm vào kết quả
            result.append(a[i])

            # Tăng con trỏ của a
            i += 1

        else:

            # Thêm phần tử của b vào kết quả
            result.append(b[j])

            # Tăng con trỏ của b
            j += 1

    # Thêm các phần tử còn lại của a (nếu có)
    while i < len(a):
        result.append(a[i])
        i += 1

    # Thêm các phần tử còn lại của b (nếu có)
    while j < len(b):
        result.append(b[j])
        j += 1

    # Trả về danh sách đã trộn
    return result


# Hai danh sách đã sắp xếp
a = [1, 3, 5]
b = [2, 4]

# In kết quả
print(merge_sorted(a, b))