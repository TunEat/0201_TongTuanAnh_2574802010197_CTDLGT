class Person:
    def __init__(self):
        self.arr =[]
    def them(self,value):
        self.arr.append(value)
    def xoa(self):
        self.arr.pop()


a = Person()
a.them(1)
a.them(2)
a.them(3)

print(f'phan tu cuoi la {a.arr[-1]}')
a.xoa()
print(f"popback la {a.arr}")






