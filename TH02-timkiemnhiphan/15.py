def gannhat(a,x,k):
    #k la so luong phan tu can tim
    #x la gia tri can tim 
    list = []
    for j  in range(len(a)):#0 den len(a) - 1
        min = 0
        if (x - a[j]) > min:
            min = (x-a[j])
        if min == 1 or min == 0:#dk kiem tra xem co phai phan tu gan x ko
            list.append(a[j])
        if len(list) == k:#kiem tra xem du phan tu can tim chua
            break
    print(list)


            
a = [1,2,3,4,5]
gannhat(a,3,4)