#bài 10 vị trí xuất hiện cuối cùng
def vitricuoi (a,x):
    for i in range(n-1,0,-1):
        if a[i] == x:
            print(f"Vị trí cuối cùng của {x} là {i}")

a = [1,3,5,1,9]
x = 1
n = len(a)
vitricuoi(a,x)
