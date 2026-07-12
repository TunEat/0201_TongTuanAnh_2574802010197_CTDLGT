#bài 2 sắp xếp tăng dần cơ bản
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j+1],a[j] = a[j],a[j+1]
    return a
a = [5,1,4,2,8]
print(bubble_sort(a))