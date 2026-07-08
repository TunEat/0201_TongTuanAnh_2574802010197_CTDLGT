#bài 16 phần tử gần nhất
def gan_nhat(a,x): 
    gan = a[0]
    vitri = 0
    for i in range(n):
        if abs(a[i] - x) < abs(gan -x):
            gan = a[i]
            vitri = i
    print(f'Phần tử gần {x} và vị trí là {gan} và {vitri}')

a =[10,22,28,29,40]
n = len(a)
gan_nhat(a,26)