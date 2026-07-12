#bài 8 tìm chỉ số nhỏ nhất trong đoạn [i,n)
def timkiem(a,k):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[min] == k:
                min = k
    print(min)
a = [9,3,7,1,5]
timkiem(a,1)