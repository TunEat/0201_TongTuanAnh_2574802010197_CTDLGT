#bài 6 phần tử nào về đúng chỗ sau 1 lượt
def bubble_sort(a):
    for i in range(1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    #[2,4,1,3,7] mảng lúc này

    print(f'Giá trị cuối mảng là {a[-1]}')

a = [4,2,7,1,3]
bubble_sort(a)