#bai 4b
# Hàm băm
def hash_mod(k, m):
    return k % m
# Hàm đếm va chạm
def count_collision(keys, m):
    buckets = {}      # Lưu số phần tử trong mỗi bucket
    collision = 0     # Đếm số va chạm

    # Duyệt từng khóa
    for key in keys:

        # Tính bucket của khóa
        index = hash_mod(key, m)

        # Nếu bucket đã có phần tử thì xảy ra va chạm
        if index in buckets:
            collision += 1
            buckets[index] += 1
        else:
            buckets[index] = 1

    return collision


# Danh sách khóa
keys = [17, 27, 37, 42]

# Số bucket
m = 10

# In số va chạm
print("Số va chạm:", count_collision(keys, m))