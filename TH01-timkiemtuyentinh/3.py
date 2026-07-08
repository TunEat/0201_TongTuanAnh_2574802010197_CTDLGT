#bài 7 kiểm tra tồn tại
def ton_tai(a,n,x):
    for i in range(0,n):
        if a[i] == x:
            return True
        return False

a = [1,2,3,4,5,6]
x = 1
n = len(a)
result = ton_tai(a,n,x)
print(result)