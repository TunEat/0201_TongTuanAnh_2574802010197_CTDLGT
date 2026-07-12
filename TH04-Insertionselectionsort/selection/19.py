def double_selection_sort(a):
    l, r = 0, len(a) - 1
    while l < r:
        mi = ma = l
        for i in range(l, r + 1):
            if a[i] < a[mi]: mi = i
            if a[i] > a[ma]: ma = i
        
        a[l], a[mi] = a[mi], a[l]
        if ma == l: ma = mi # Bắt biên: Nếu max nằm ở đầu, nó đã bị đẩy sang vị trí mi
        a[r], a[ma] = a[ma], a[r]
        l, r = l + 1, r - 1
    return a
double_selection_sort(a)