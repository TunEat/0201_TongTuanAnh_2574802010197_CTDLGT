def timkiem(a, k):
    s = 0
    e = len(a) - 1 #4
    while s <= e:
        mid = (s + e) // 2
        missing = a[mid] - (mid + 1)
        if missing < k:
            s = mid + 1
        else:
            e = mid - 1

    return s + k

a = [2,3,4,7,11]
print(timkiem(a, 5))
#[1,2,3,4,5,6,7,8,9,10,11]
#[1,5,6,8,9,10]