#đếm số lần so sánh
def sosanh(a):
    count = 0
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        
        while j >= 0:
            count += 1
            if key < a[j]:
                a[j+1] = a[j]
                j-= 1
            else:
                break
        
        a[j+1] = key
    print(count)


a = [1,2,3]
sosanh(a)
print(a)
