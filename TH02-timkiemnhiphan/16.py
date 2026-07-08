def gannhat(a, x, k):

    ds = []

    for i in range(len(a)):

        khoang_cach = a[i] - x

        if khoang_cach < 0:
            khoang_cach = -khoang_cach

        ds.append([khoang_cach, a[i]])

    for i in range(len(ds)):

        for j in range(len(ds)-1-i):

            if ds[j][0] > ds[j+1][0]:

                ds[j], ds[j+1] = ds[j+1], ds[j]

    ketqua = []

    for i in range(k):

        ketqua.append(ds[i][1])

    for i in range(len(ketqua)):

        for j in range(len(ketqua)-1-i):

            if ketqua[j] > ketqua[j+1]:

                ketqua[j], ketqua[j+1] = ketqua[j+1], ketqua[j]

    print(ketqua)


a = [1,2,3,4,5]
gannhat(a,5,2)