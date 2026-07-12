#bài 9 binary insertion sort
def binary_search(a, key, left, right):
    while left <= right:
        mid = (left + right) // 2
        if key < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left


def binary_insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]

        # Tìm vị trí chèn bằng tìm kiếm nhị phân
        pos = binary_search(a, key, 0, i - 1)

        # Dịch chuyển các phần tử
        j = i - 1
        while j >= pos:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

        print(f"Bước {i}: {a}")


a = [5, 2, 4, 6, 1, 3]
binary_insertion_sort(a)

print("Kết quả:", a)