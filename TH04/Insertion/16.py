#bài 16 sắp xếp trực tuyến (online)
def online_insertion(a, x):
    a.append(x)

    i = len(a) - 1

    while i > 0 and a[i] < a[i-1]:
        a[i], a[i-1] = a[i-1], a[i]
        i -= 1

a = []

n = int(input("Nhập số lượng phần tử: "))

for i in range(n):
    x = int(input("Nhập số: "))
    online_insertion(a, x)
    print("Mảng sau khi chèn:", a)