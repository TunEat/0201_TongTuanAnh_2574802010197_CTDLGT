#số shift = số nghịch thế 
def shift(a):
    count = 0
    for i in range(1,len(a)):
        b = a[i]
        j = i - 1
        while j >= 0 and b < a[j]:
            a[j+1] = a[j]
            j-= 1
            count += 1
        a[j+1] = b
    print(a)
    print(count)

a = [2,4,1,3]   
shift(a) 

def nghichthe(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                count += 1
                a[i],a[j]=a[j],a[i]
    print(count)
    print(a)
a = [2,4,1,3]     
nghichthe(a)