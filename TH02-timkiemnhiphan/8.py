def can():
    n = int(input("Nhap so nguyen: "))
    while n < 0:
        n = int(input("Vui long nhap so >= 0: "))
    i = 0
    while i * i <= n:
        i += 1
    print(i - 1)
can()