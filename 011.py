#Bubble Sort
def bubble_sort(arr): #tạo hàm 
    for i in range(len(arr)): #tạo vòng lặp theo số phần tử trong mảng arr
        for j in range(len(arr)-1): #tạo vòng lặp 
            if arr[j] > arr[j+1]: #nếu đúng
                arr[j],arr[j+1] = arr[j+1],arr[j]
                #hoán đổi hai vị trí arr[j] và arr[j+1]
                #thì hiện tại mảng là [35,120,60,42,...]
   


arr = [120,35,60,42,280,7,15,19]
bubble_sort(arr)
print(arr)
