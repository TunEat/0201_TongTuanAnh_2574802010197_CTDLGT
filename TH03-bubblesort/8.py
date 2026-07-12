#bài 8 kiểm tra đã sắp xếp sau k lượt
def sapxep(a,k):
    for i in range(k):
        for j in range(len(a)-1):
            if a[i] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    for k in range(len(a)-1):
            if a[k] > a[k+1]:
                return False
            else:
                return True
    print(a)
a = [3,2,1]
print(sapxep(a,1)) #nếu k là 3 thì sẽ True vì mảng đã được sắp xếp hoàn chỉnh