#bài 19 Gnome sort
def sapxep(a):
    i = 0
    while i < len(a):#điều kiện dừng 
        if i == 0 or a[i] >= a[i-1]:
            i += 1
            #1
            #2
            #3
        else:
            a[i],a[i-1]=a[i-1],a[i]
            i -= 1
    print(a)

a = [3,2,1]    
#[2,3,1]
#[2,1,3]
#[1,2,3]
sapxep(a)