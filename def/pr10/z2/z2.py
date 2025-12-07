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


def read_matrix_from_file(filename):

    matrix = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Разделяем строку на числа, убирая пробелы и пустые значения
                row = [int(x) for x in line.strip().split() if x]
                if row:  # Добавляем только непустые строки
                    matrix.append(row)
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return []
    except ValueError:
        print("Ошибка: в файле содержатся нечисловые данные!")
        return []
    
    return matrix


def write_matrix_to_file(filename, matrix, original_matrix=None):
    """Запись матрицы в файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("=" * 60 + "\n")
            file.write("Дана матрица B[N, М]. Найти в каждой строке матрицы максимальный и минимальный элементы и поменять их с первым и последним элементами строки соответственно.\n")
            file.write("=" * 60 + "\n\n")
            
            if original_matrix:
                file.write("Исходная матрица:\n")
                for row in original_matrix:
                    file.write(" ".join(str(x) for x in row) + "\n")
                file.write("\n")
            
            file.write("После обработки:\n")
            for row in matrix:
                file.write(" ".join(str(x) for x in row) + "\n")
        
        print(f"Результат успешно записан в файл: {filename}")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")


def main():
    # Чтение матрицы из файла
    input_filename = "C:/Users/Полина/Desktop/Универ/def/pr10/z2/imshenetskayaPA_um252_vvod.txt"
    output_filename = "C:/Users/Полина/Desktop/Универ/def/pr10/z2/imshenetskayaPA_um252_vvod.txt"
    
    # Читаем исходную матрицу
    matrix = read_matrix_from_file(input_filename)
    
    if not matrix:
        print("Не удалось прочитать матрицу из файла.")
        return
    
    print("=" * 60)
    print("Дана матрица B[N, М]. Найти в каждой строке матрицы максимальный и минимальный элементы и поменять их с первым и последним элементами строки соответственно.")
    print("=" * 60)
    
    # Сохраняем копию оригинальной матрицы для вывода
    original_matrix = [row.copy() for row in matrix]
    
    print("Исходная матрица:")
    for row in original_matrix:
        print(row)
    
    # Обрабатываем матрицу
    process_matrix_optimized(matrix)
    
    print("\nПосле обработки:")
    for row in matrix:
        print(row)
    
    # Записываем результат в файл
    write_matrix_to_file(output_filename, matrix, original_matrix)


if __name__ == "__main__":
    main()