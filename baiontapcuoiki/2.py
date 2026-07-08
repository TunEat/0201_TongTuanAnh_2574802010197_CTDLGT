A = [5, 2, 4, 6, 1, 3]
# Insertion Sort
def insertion_s(A):
    shift = 0  # Đếm số lần dịch chuyển
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]   # Dịch phần tử sang phải
            shift += 1         # Tăng số lần dịch chuyển
            j -= 1
        A[j + 1] = key

    print("Mảng sau khi sắp xếp:", A)
    print("Số lần dịch chuyển:", shift)

insertion_s(A)

#cac cap nghich the la mot cap phan tu
#(A[i],A[j]) sao cho i <j va A[i] > A[j]
#thi chung ta co (5,2),(5,4),(5,1),(5,3),(2,1),(4,1),.... => 9 nghich the 
    