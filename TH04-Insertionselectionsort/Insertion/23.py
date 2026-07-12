#bai 23
def insertionSort(a):
    soSanh = 0
    shift = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            soSanh += 1

            if a[j] > key:
                a[j + 1] = a[j]
                shift += 1
                j -= 1
            else:
                break

        a[j + 1] = key

    print("Mảng sau khi sắp xếp:", a)
    print("Số lần so sánh:", soSanh)
    print("Số lần shift:", shift)

a = [1,2,3,4,5]
#so lan so sanh it va do phuc tap la O(n)
print("Best Case")
insertionSort(a)

#a = [5,2,4,6,1,3]
#print("Average Case")
#so lan so sanh trung binh va do phuc tap la O(n**2)



#a = [5,4,3,2,1]
#print("Worst Case")
#so lan so sanh nhieu do phuc tao la O(n**2)
