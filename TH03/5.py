#bài 5 đếm số lần so sánh
def solanss(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            count +=1 
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                
    print(f'so lan so sanh la {count}')
    print(a)
a = [3,2,1]
solanss(a)

