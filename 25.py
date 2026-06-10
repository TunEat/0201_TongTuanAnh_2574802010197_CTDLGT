def maxForce(x, m):
    max_d = 0
    vitri_totnhat = []
    for d in range(1, x[len(x)-1] - x[0] + 1):
        vitri = [x[0]]
        count = 1
        last = x[0]
        for i in range(1, len(x)):
            if x[i] - last >= d:
                vitri.append(x[i])
                count += 1
                last = x[i]
        if count >= m:
            max_d = d
            vitri_totnhat = vitri[:m]
    print("Lực từ lớn nhất:", max_d)
    print("Vị trí đặt:", vitri_totnhat)

x = [1,2,3,4,7]
maxForce(x, 3)

