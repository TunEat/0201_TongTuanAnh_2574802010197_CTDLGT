#bài 4 đếm số lần hoán đổi 
def solandoi(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                count += 1
    print('Số lần là',count)
    print(a)

a = [3,2,1]
solandoi(a)   