def gannhat(a,x,k):
    list = []
    for j  in range(len(a)):
        min = 0
        if (x - a[j]) > min:
            min = (x-a[j])
        if min == 1 or min == 0:
            list.append(a[j])
        if len(list) == k:
            break
    print(list)


            
a = [1,2,3,4,5]
gannhat(a,3,4)