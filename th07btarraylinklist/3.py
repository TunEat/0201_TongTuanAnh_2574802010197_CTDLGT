class mang:
    def __init__(self):
        self.arr = []
    def chen(self,so,vitri):
        for i in range(len(self.arr)):
            if i == vitri:
                self.arr[i].append(so)
    def them(self,giatri):
        self.arr.append(giatri)
        
a = mang()
a.them(1)
a.them(2)
a.them(4)

a.chen(3,2)
print(f"sau khi chen la {a.arr}")
