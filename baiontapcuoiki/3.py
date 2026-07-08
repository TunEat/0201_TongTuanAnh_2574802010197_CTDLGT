# Đồ thị có hướng gồm 3 đỉnh
# Đồ thị có hướng
# Đồ thị
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [],
    'C': [('B', -4)]
}

# Dijkstra sau khi chốt B
dijkstra = {
    'A': 0,
    'B': 2,
    'C': 5
}

print("Kết quả Dijkstra:")
print("A -> B =", dijkstra['B'])

# Kiểm tra đường đi khác
duong_di = 5 + (-4)

print("\nĐường đi A -> C -> B =", duong_di)

if duong_di < dijkstra['B']:
    print("\n=> Dijkstra SAI")
    print("Vì Dijkstra cho A -> B =", dijkstra['B'])
    print("Trong khi đường đi ngắn nhất là", duong_di)
    print("Nguyên nhân: B đã bị chốt nên không được cập nhật.")


#Thuật toán Dijkstra giả sử rằng khi một đỉnh đã được chốt, khoảng cách từ đỉnh 
# nguồn đến đỉnh đó đã là ngắn nhất và sẽ không thay đổi nữa. Giả thiết này chỉ 
# đúng khi tất cả các cạnh đều có trọng số không âm.à tối ưu" không còn đúng.

#Nếu có cạnh trọng số âm, sau khi một đỉnh đã được chốt vẫn có thể xuất hiện một đường 
# đi ngắn hơn đi qua cạnh âm. Tuy nhiên, Dijkstra sẽ không cập nhật lại đỉnh đã chốt, nên kết quả có thể sai.

#Thuật toán thay thế: Bellman-Ford, vì thuật toán này 
# vẫn tìm đúng đường đi ngắn nhất trên đồ thị có cạnh 
# trọng số âm (và còn phát hiện được chu trình âm).