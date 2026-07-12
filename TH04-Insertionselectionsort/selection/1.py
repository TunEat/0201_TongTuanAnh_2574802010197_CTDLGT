#bài 1 tìm phần tử nhỏ nhất đưa về đầu
def sapxep(a):
    min = 0
    for j in range(len(a)):
        if a[min] > a[j]:
            min = j
    a[0],a[min]=a[min],a[0]
    
    print(a)


a = [4,2,7,1,3]
sapxep(a)