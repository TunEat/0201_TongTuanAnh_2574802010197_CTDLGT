def nhonhat():
    min = a[0]
    for i in range(len(a)):
       if a[i] < min:
           min = a[i]
           print(f"Giá trị nhỏ nhất trong mảng là {min}")
a = [3,4,5,1,2]
nhonhat()