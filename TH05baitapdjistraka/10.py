#bài 10
def choose_method(V,E):

    if E > V*V//2:
        print("Dùng ma trận + O(V^2)")
    else:
        print("Dùng heap + O((V+E)logV)")

choose_method(1000,100000)