def process_matrix_optimized(matrix):
    
    for i, row in enumerate(matrix):
        if len(row) == 0:
            continue
            
        if len(row) == 1:
            continue  
            
        max_val = row[0]
        min_val = row[0]
        max_idx = 0
        min_idx = 0
        
        for j in range(1, len(row)):
            if row[j] > max_val:
                max_val = row[j]
                max_idx = j
            if row[j] < min_val:
                min_val = row[j]
                min_idx = j
        
        row[0], row[max_idx] = row[max_idx], row[0]
        
        if min_idx == 0:
            min_idx = max_idx
        elif min_idx == max_idx:
            min_idx = 0
        
        last_idx = len(row) - 1
        row[last_idx], row[min_idx] = row[min_idx], row[last_idx]
    
    return matrix

matrix = [
    [5, 8, 3, 9, 2],
    [10, 4, 6, 1, 7],
    [3, 3, 3, 3, 3]
]

print("="*60)
print("Дана матрица B[N, М]. Найти в каждой строке матрицы максимальный и минимальный элементы и поменять их с первым и последним элементами строки соответственно. ")
print("="*60)

print("Исходная матрица:")
for row in matrix:
    print(row)

process_matrix_optimized(matrix)

print("\nПосле обработки:")
for row in matrix:
    print(row)