#bài 12 min max trong 1 lần duyệt
def min_max (a):
    min = a[0]
    max = a[0]
    for i in a:
        if i < min:
            min = i
        if i > max:
            max = i
    print(f"Max và Min lần lượt là {max} và {min}")
a = [1,6,3,9,5]
min_max(a)
