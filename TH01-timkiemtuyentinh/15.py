#bai 20 
danhBa = []#tao ds rong
#khi chung ta them lien he thi se them vao ds danhBa
#trong danhBa no se co dang
#danhBa=[
 #{"ten":"An","sdt":"090"},
 #{"ten":"Bình","sdt":"091"}]

while True:#lap cho den khi gap break
    print("\n===== QUẢN LÝ DANH BẠ =====")
    print("1. Thêm liên hệ")
    print("2. Tìm số điện thoại theo tên")
    print("3. Tìm tên theo số điện thoại")
    print("4. Đếm số liên hệ có đầu số cho trước")
    print("5. Thoát")

    chon = input("Nhập lựa chọn: ")#lua chon chuc nang

    if chon == "1":#them thong tin vao danhBa
        ten = input("Nhập tên: ")#ten
        sdt = input("Nhập số điện thoại: ")#sdt
        danhBa.append({"ten": ten, "sdt": sdt})#them vao danhBa
        print("Đã thêm liên hệ!")

    elif chon == "2":#tim sdt theo ten
        ten = input("Nhập tên cần tìm: ")
        timThay = False
        for i in danhBa:#duyet trong danhBa
            if i["ten"] == ten:
                print("Số điện thoại:", i["sdt"])
                timThay = True
                break
        if not timThay:#neu timThay van la False tuc la ko tim thay
            print("Không tìm thấy!")

    elif chon == "3":
        sdt = input("Nhập số điện thoại cần tìm: ")
        timThay = False
        for i in danhBa:
            if i["sdt"] == sdt:
                print("Tên:", i["ten"])
                timThay = True
                break
        if not timThay:
            print("Không tìm thấy!")

    elif chon == "4":#tim so luong sdt co 3 so dau
        n = input("Nhập đầu số: ")
        dem = 0
        for i in danhBa:
            if i["sdt"].startswith(n):
                dem += 1
        print("Có", dem, "liên hệ có đầu số", n)

    elif chon == "5":
        print("Kết thúc chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")