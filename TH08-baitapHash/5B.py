#bai 5
# Hàm băm
def hash_mod(k, m):
    return k % m
# Hàm in phân bố các khóa vào bucket
def distribution(keys, m):
    buckets = {}

    # Tính bucket của từng khóa
    for key in keys:
        index = hash_mod(key, m)

        if index not in buckets:
            buckets[index] = []

        buckets[index].append(key)

    # In kết quả
    print("m =", m)
    for bucket in sorted(buckets):
        print("Bucket", bucket, ":", buckets[bucket])
    print()


# Tập khóa
keys = [16, 32, 48, 64, 80]

distribution(keys, 16)
distribution(keys, 17)


#Với:
#16 % 16 = 0
#32 % 16 = 0
#48 % 16 = 0
#64 % 16 = 0
#80 % 16 = 0
#Bucket 0 : [16, 32, 48, 64, 80] tất cả các khóa rơi vào cùng một bucket, xảy ra rất nhiều va chạm.

#16 % 17 = 16
#32 % 17 = 15
#48 % 17 = 14
#64 % 17 = 13
#80 % 17 = 12

#Bucket 16 : [16]
#Bucket 15 : [32]
#Bucket 14 : [48]
#Bucket 13 : [64]
#Bucket 12 : [80]Các khóa được phân bố đều vào nhiều bucket khác nhau.