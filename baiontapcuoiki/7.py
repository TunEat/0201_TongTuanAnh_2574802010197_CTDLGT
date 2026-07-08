A = [3, 4, 7, 2, -3, 1, 4, 2]
S = 7#muc tieu

prefix = 0
count = 0 #dem so mang con co tong bang 7 (S)

hashMap = {0: 1}
#{0:1, 3:1, 7:1, 14:2, 16:1, 13:1, 18:1, 20:1}

for x in A:
    prefix += x
    #3 7 14 16 13 14 18 20

    if prefix - S in hashMap:#no kiem tra xem co ton tai prefix-S trong hashMap hay khong
        #neu co thi dem so lan xuat hien cua prefix-S trong hashMap va cong vao count
        count += hashMap[prefix - S]

    hashMap[prefix] = hashMap.get(prefix, 0) + 1

print("Số mảng con có tổng bằng", S, "=", count)
#Có 4 mảng con liên tiếp có tổng bằng 7:
#[3,4]
#[7]
#[7,2,-3,1]
#[1,4,2]

#Kết luận: Thuật toán sử dụng Mảng cộng dồn (Prefix Sum) 
#để tính tổng từ đầu mảng đến từng vị trí và Bảng băm (Hash Map) 
#để lưu các giá trị Prefix Sum đã xuất hiện. Trong quá trình duyệt mảng, 
# nếu prefix - S đã có trong Hash Map thì chứng tỏ tồn tại một hoặc nhiều mảng con liên tiếp có tổng bằng S, và cập nhật biến đếm count.