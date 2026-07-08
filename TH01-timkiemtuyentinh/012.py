def tuyen_tinh(array,n,x):
    for i in range(0,n):
        if (array[i] == x):
            return i
    return -1
array = [15,25,80,30,60,50,110,100,130,180]
x = 110
n = len(array)
result = tuyen_tinh(array,n,x)
if result == -1:
    print(f"Phan tu khong tim thay trong arr[] , {result}")
else:
    print(f"Phần tử tìm thấy ở vị trí là {result}")


