#chèn từ cuối hay đầu
def insertion_right(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a
#dò từ phải sang trái ít kiểm tra 

a = [5, 2, 4, 6, 1, 3]
print(insertion_right(a))
def insertion_left(a):
    for i in range(len(a) - 2, -1, -1):
        key = a[i]
        j = i + 1

        while j < len(a) and a[j] < key:
            a[j - 1] = a[j]
            j += 1

        a[j - 1] = key

    return a


a = [5, 2, 4, 6, 1, 3]
print(insertion_left(a))#dò từ trái sang phải thường phải kiểm tra nhiều hơn khi dữ liệu gần như đã sắp xếp
