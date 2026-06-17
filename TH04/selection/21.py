#bài 21
def count_selection_sort_comparisons(arr):
    a = arr[:]
    n = len(a)
    comparisons = 0
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1  # Đếm mỗi lần thực hiện so sánh
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        
    return comparisons

# Chạy thử nghiệm với n = 5 (Kỳ vọng số phép so sánh là 5*(5-1)/2 = 10)
n = 5
best_case = [1, 2, 3, 4, 5]
worst_case = [5, 4, 3, 2, 1]
random_case = [3, 5, 1, 4, 2]

print(f"Số phép so sánh (Best case):   {count_selection_sort_comparisons(best_case)}")
print(f"Số phép so sánh (Worst case):  {count_selection_sort_comparisons(worst_case)}")
print(f"Số phép so sánh (Random case): {count_selection_sort_comparisons(random_case)}")