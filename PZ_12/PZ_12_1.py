# В матрице найти сумму элементов первых двух строк
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

        # Генераторное выражение для ленивого вычисления суммы первых двух строк
        limit = 2 if rows >= 2 else rows
        sum_first_two = sum(x for row in matrix[:limit] for x in row)
        print(f"\nСумма элементов первых двух строк: {sum_first_two}")

    except ValueError:
        print("\nОшибка ввода: пожалуйста, введите целые числа.")


if __name__ == "__main__":
    main()