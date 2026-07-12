def solan(a):
    dem  = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                dem += 1
    print(a)
    print(f'{dem}')


a = [1,2,4,5,3]    
solan(a)