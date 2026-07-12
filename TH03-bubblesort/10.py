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
a = [2,1,3,4]
bubble_sort(a)
