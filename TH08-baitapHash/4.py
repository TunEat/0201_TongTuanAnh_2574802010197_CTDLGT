def common_elements(A, B):
    # Chuyển mảng A thành tập hợp (set) để tìm kiếm nhanh O(1)
    setA = set(A)

    # Tạo tập hợp rỗng để lưu các phần tử chung
    result = set()

    # Duyệt từng phần tử trong mảng B
    for x in B:

        # Nếu x có trong tập hợp setA
        if x in setA:

            # Thêm x vào kết quả
            # Dùng set nên tự động loại bỏ phần tử trùng
            result.add(x)

    # Trả về tập hợp các phần tử chung
    return result

# Mảng thứ nhất
A = [1, 2, 3]
# Mảng thứ hai
B = [2, 3, 4]
# Gọi hàm và in kết quả
print(common_elements(A, B))
# Kết quả:
# {2, 3}