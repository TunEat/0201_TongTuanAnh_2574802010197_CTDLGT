#bài 17 phần tử nhỏ thứ k
def tim_nho_thu_k(a, k):
    da_chon = [False] * len(a)

    for dem in range(k):
        min = -1
        for i in range(len(a)):
            if not da_chon[i]:
                if min == -1 or a[i] < a[min]:
                    min = i

        da_chon[min] = True

    return a[min]

a = [7, 2, 5, 1, 9]
k = 3

print(tim_nho_thu_k(a, k))
print(a)