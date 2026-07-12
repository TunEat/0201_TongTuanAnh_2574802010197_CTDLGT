#bai 19
ds= [{"maSV": "SV01", "hoTen": "Nguyen Van A", "diemTB": 8.5},
    {"maSV": "SV02", "hoTen": "Tran Thi B", "diemTB": 7.8},
    {"maSV": "SV03", "hoTen": "Le Van C", "diemTB": 9.0}]

def timSinhVien(a):
    for i in ds:
        if i["maSV"] == a:#lay gia tri maSV trong ds
            #neu co thi print ra thong tin sinh vien
            print("Mã SV:", i["maSV"])
            print("Họ tên:", i["hoTen"])
            print("Điểm TB:", i["diemTB"])
            return
    print("Không tìm thấy sinh viên!")

n = input("Nhập mã sinh viên cần tìm: ")
timSinhVien(n)