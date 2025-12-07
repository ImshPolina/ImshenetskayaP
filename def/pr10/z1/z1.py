def main():
    input_file = "C:/Users/Полина/Desktop/Универ/def/pr10/z1/imshenetskayaPA_um252_vvod.txt"
    output_file = "C:/Users/Полина/Desktop/Универ/def/pr10/z1/imshenetskayaPA_um252_vivod.txt"
    
    try:
        # Чтение матрицы
        with open(input_file, 'r') as f:
            matrix = [[int(num) for num in line.split()] for line in f]
        
        n = len(matrix)
        
        # Вычисления
        sum_pos = 0
        count_pos = 0
        
        for i in range(n):
            for j in range(n):
                if j > i and matrix[i][j] > 0:
                    sum_pos += matrix[i][j]
                    count_pos += 1
        
        # Запись результатов
        with open(output_file, 'w', encoding="utf-8") as f:
            f.write(f"Размер матрицы: {n}x{n}\n")
            f.write(f"Положительных элементов над диагональю: {count_pos}\n")
            f.write(f"Их сумма: {sum_pos}\n")
        
        print(f"Готово! Результаты в файле {output_file}")
        
    except FileNotFoundError:
        print(f"Файл {input_file} не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()