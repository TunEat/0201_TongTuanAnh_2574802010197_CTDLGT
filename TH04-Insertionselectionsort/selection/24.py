# Partial Selection: lấy k phần tử nhỏ nhất
def partial_selection(arr, k):

    result = []
    a = arr.copy()

    # Lặp k lần để tìm k phần tử nhỏ nhất
    for i in range(k):

        # Tìm vị trí phần tử nhỏ nhất
        minIndex = 0

        for j in range(1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j

        # Lấy phần tử nhỏ nhất
        result.append(a[minIndex])

        # Xóa phần tử đã lấy
        a.pop(minIndex)

    return result


a = [7, 2, 9, 1, 5]
k = 3

print(partial_selection(a, k))

# Heap: lấy k phần tử nhỏ nhất
import heapq
def heap_min(arr, k):

    # Tạo min heap
    heapq.heapify(arr)

    result = []

    # Lấy k phần tử nhỏ nhất
    for i in range(k):
        result.append(heapq.heappop(arr))

    return result


a = [7, 2, 9, 1, 5]
k = 3
print(heap_min(a, k))

#k nhỏ: dùng Partial Selection vì đơn giản, ít thao tác.
#k lớn: dùng Heap vì giảm thời gian từ O(nk) xuống O(n + k log n).
#Trong thực tế, khi cần lấy nhiều phần tử nhỏ nhất, Heap thường là lựa chọn tốt hơn.

#vd n = 100000 , k =5
#k nho nen dung Partial Selection vi de cai dat va nhanh

#vd n = 100000 , k = 50000
#k lon nen dung Heap
#vi selection phai tim nho nhat 50000 lan = 100000 x 50000
#heap chi can 100000 + 50000 log(100000)