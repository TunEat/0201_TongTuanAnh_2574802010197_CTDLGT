#bài bubble sort tối ưu (early exit
def bubble_sort(a):
    count = 0
    for i in range(len(a)):
        doi = False
        count +=1
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                doi = True
        if doi == False:
            break
        
    print(a)
    print(f'so lan chay la {count}')

a = [1,2,3,4]
#1 3 2 4 luot 1
#1 2 3 4 luot 2
#1 2 3 4 luot 3 xet do khong co hoan doi nen dung vong lap
bubble_sort(a)    