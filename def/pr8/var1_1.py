import numpy as np

def calculate_positive_above_diagonal(N=5):
    
    A = np.random.randint(-10, 20, size=(N, N))
    
    print(f"Матрица A[{N}, {N}]:")
    print(A)
    print()
    
    sum_positive = 0
    count_positive = 0
    
        for i in range(N):
        for j in range(N):
            if j > i and A[i, j] > 0:  # j > i 
                sum_positive += A[i, j]
                count_positive += 1
    
    print(f"Элементы над главной диагональю (j > i):")
    for i in range(N):
        for j in range(N):
            if j > i:
                sign = "+" if A[i, j] > 0 else " "
                print(f"{sign}{A[i, j]:3} ", end="")
            else:
                print("     ", end="")
        print()
    
    print(f"\nРезультаты:")
    print(f"Число положительных элементов над главной диагональю: {count_positive}")
    print(f"Сумма положительных элементов над главной диагональю: {sum_positive}")
    
    return sum_positive, count_positive

if __name__ == "__main__":
    print("=" * 60)
    print("ВЫЧИСЛЕНИЕ СУММЫ И ЧИСЛА ПОЛОЖИТЕЛЬНЫХ ЭЛЕМЕНТОВ")
    print("НАД ГЛАВНОЙ ДИАГОНАЛЬЮ МАТРИЦЫ")
    print("=" * 60)
    
    N = 5
    result = calculate_positive_above_diagonal(N)