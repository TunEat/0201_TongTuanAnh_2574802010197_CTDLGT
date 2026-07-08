def timkiem():
    b = 0
    c = len(a) - 1
    while b < c:
        mid = (b + c)//2

        if a[mid] < a[mid + 1]:
            b +=1
        else:
            break
    print(f'Vị trí phần tử lớn hơn cả hai hàng xóm là {mid}')

a = [1,2,3,1]        
timkiem()