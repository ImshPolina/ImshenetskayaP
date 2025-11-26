import random

def generate_random_array(size=5, min_val=1, max_val=10):
    return [random.randint(min_val, max_val) for _ in range(size)]

def analyze_three_arrays():
    print("АНАЛИЗ ТРЕХ СЛУЧАЙНЫХ МАССИВОВ")
    
    arrays = [
        generate_random_array(4, 1, 5),   # массив 1
        generate_random_array(5, 1, 8),   # массив 2  
        generate_random_array(3, 1, 10)   # массив 3
    ]
    
    for i, arr in enumerate(arrays, 1):
        product = 1
        for num in arr:
            product *= num
        
        average = sum(arr) / len(arr)
        
        print(f"\nМассив {i}: {arr}")
        print(f"Количество элементов: {len(arr)}")
        print(f"Сумма элементов: {sum(arr)}")
        print(f"Произведение элементов: {product}")
        print(f"Среднеарифметическое: {average:.2f}")
        print(f"Минимальный элемент: {min(arr)}")
        print(f"Максимальный элемент: {max(arr)}")

analyze_three_arrays()