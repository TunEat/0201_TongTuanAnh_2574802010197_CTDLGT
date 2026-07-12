def swap(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                count +=1
    print(f'So lan doi la {count}')

a = [2,3,1]
swap(a)    

def nghichthe(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                count += 1
    print(f'So nghich the {count}')

a = [2,3,1]
nghichthe(a)   