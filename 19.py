def cows(x, c):

    s = 1
    e = x[len(x)-1] - x[0]
    ans = 0
    while s <= e:
        mid = (s + e) // 2
        dem = 1
        vitri_cuoi = x[0]
        for i in range(1, len(x)):
            if x[i] - vitri_cuoi >= mid:
                dem += 1
                vitri_cuoi = x[i]
        if dem >= c:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    return ans
x = [1,2,4,8,9]
c = 3

print(cows(x, c))