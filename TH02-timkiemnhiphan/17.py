def ship(w, D):

    s = w[0]
    for i in range(len(w)):
        if w[i] > s:
            s = w[i]
    e = 0
    for i in range(len(w)):
        e += w[i]
    while s <= e:
        mid = (s + e) // 2
        ngay = 1
        tong = 0
        for i in range(len(w)):
            if tong + w[i] <= mid:
                tong += w[i]
            else:
                ngay += 1
                tong = w[i]
        if ngay <= D:
            e = mid - 1
        else:
            s = mid + 1
    return s

w = [1,2,3,4,5,6,7,8,9,10]
D = 5

print(ship(w, D))