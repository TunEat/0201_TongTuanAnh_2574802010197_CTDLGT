#bài 6 hàm tìm kiếm cơ bản
def linear_search(a,x):
    for i in range(n):
        if a[i] == x:
            return i
    return -1

a = [1,4,7,9]
x = 1
n =len(a)
print(linear_search(a,x))
