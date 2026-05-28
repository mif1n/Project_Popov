# В матрице найти минимальный и максимальный элементы
import random


def main():
    try:
        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))

        # Генерация матрицы через списковое включение
        matrix = [[random.randint(-20, 30) for _ in range(cols)] for _ in range(rows)]

        print("\nИсходная матрица:")
        for row in matrix:
            print(row)

        # Списковое включение для получения всех элементов матрицы в плоский список
        flat_elements = [x for row in matrix for x in row]

        print(f"\nМинимальный элемент: {min(flat_elements)}")
        print(f"Максимальный элемент: {max(flat_elements)}")

    except ValueError:
        print("\nОшибка ввода: пожалуйста, введите целые числа.")


if __name__ == "__main__":
    main()