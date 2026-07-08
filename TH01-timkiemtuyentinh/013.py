def linearsearch (arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
arr = ['Bảo','An','Dat','Duc','Hung','Phi','Vinh','Dung']
key = 'Phi'
print("Vị trí tìm thấy thứ i là:" +str(linearsearch(arr,key)))