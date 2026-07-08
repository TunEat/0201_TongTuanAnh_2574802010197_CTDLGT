def donle():
    for i in range(len(a)):
        dem = 0
        for j in range(len(a)):
            if a[i] == a[j]:
                dem +=1 
        if dem == 1:
            print(f'Phần tử đơn lẻ là {a[i]}')
              


a = [1,1,2,3,3,4,4]
donle()
