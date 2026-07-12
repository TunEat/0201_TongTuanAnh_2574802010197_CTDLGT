class DanhSach:
    def __init__(self):
        self.chua = 4          #khởi tạo sức chứa ban đầu của mảng
        self.sophantu = 0      #cho biết số phần tử đang có trong mảng
        self.arr = [None] * self.chua #None để biết sức chứa mảng hiện tại tới khúc nào dựa trên input của n 

    def them(self, giatri): #hàm để xem coi mảng đã đầy chưa
        if self.sophantu == self.chua:#nếu đầy chạy code bên trong
            print("Mảng đầy")
            print("Tăng sức chứa từ", self.chua, "lên", self.chua * 2)
            self.tangsucchua()#gọi hàm

        # Thêm phần tử vào mảng
        self.arr[self.sophantu] = giatri
        self.sophantu += 1

    def tangsucchua(self):
        self.chua *= 2#tăng sức chứa gấp đôi
    
        arr1 = [None] * self.chua#tạo 1 mảng mới gán tất cả là None

        for i in range(self.sophantu):#lặp qua số phần tử
            arr1[i] = self.arr[i] #chuyển giá trị bên arr sang arr1 mảng mới 

        # Thay mảng cũ bằng mảng mới
        self.arr = arr1

    def xuatketqua(self):
        print("\nMảng sau khi thêm:")
        print(self.arr)
        print("Số phần tử:", self.sophantu)
        print("Sức chứa:", self.chua)

# Chương trình chính
n = int(input("Nhập số lượng phần tử: "))
a = DanhSach()

for i in range(n):#lặp dựa trên input n
    a.them(i)
a.xuatketqua()

