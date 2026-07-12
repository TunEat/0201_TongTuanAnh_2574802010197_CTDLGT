a = []
def tuyentinh(a,x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1 
def them(c):
    a.append(c)

them(5)         
them(5)   
them(7)   

x=7
i=tuyentinh(a,7)
print(f'vi tri tim thay {x} la {i}')