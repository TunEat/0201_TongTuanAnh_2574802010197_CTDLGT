W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#khoi luong cua tat ca kien hang2

K = 5#so xe tai

def xe(limit):
    xe = 1  #xe 1
    hientai = 0 #khoi luong hien tai cua xe

    for w in W:
        if hientai + w <= limit:#neu khong vuot tai trong thi tiep tuc them kien hang
            hientai += w

        else:#neu vuot khoi luonh hien tai cua xe chuyen qua xe thu 2,.....
            xe += 1#thi +1 chuyen sang xe thu 2,...
            hientai = w

    return xe <= K#tra ve true neu so xe <= K
#vi k = 5 nen phai tim tai trong nho nhat de chuyen het hang trong 1 luot

left = max(W)#10
right = sum(W)#55

while left < right:#lap cho den khi left = right
    mid = (left + right) // 2
    if xe(mid):#neu true thi chay code ben trong
        right = mid
    else:
        left = mid + 1

print("Tải trọng nhỏ nhất:", left)