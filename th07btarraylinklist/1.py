class danhsach:
    def __init__(self):
        self.a =[]

    def add(self,giatri):
        self.a.append(giatri)

    def get(self,vitri):
        return self.a[vitri]

a = danhsach()
n = int(input("Nhập số lượng:"))
for i in range(n):
    a.add(i)
print(a.get(2))
        
        

