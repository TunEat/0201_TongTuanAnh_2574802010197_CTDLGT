#bai 8
# Hàm xóa các số chẵn khỏi mảng
def remove_even(arr):

    # Con trỏ ghi, chỉ vị trí sẽ lưu phần tử hợp lệ
    write = 0

    # Con trỏ đọc, duyệt toàn bộ mảng
    for read in range(len(arr)):

        # Nếu là số lẻ thì giữ lại
        if arr[read] % 2 != 0:

            # Ghi phần tử vào vị trí write
            arr[write] = arr[read]

            # Tăng vị trí ghi
            write += 1

    # Xóa các phần tử dư ở cuối mảng
    del arr[write:]


# Mảng ban đầu
a = [1, 2, 3, 4]

# Gọi hàm xóa số chẵn
remove_even(a)

# In mảng sau khi xóa
print(a)