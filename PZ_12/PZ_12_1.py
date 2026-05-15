#В матрице найти сумму элементов первых двух строк.

from functools import reduce

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def sum_first_two_rows(matrix):
    if len(matrix) < 2:
        raise ValueError("Матрица должна содержать минимум 2 строки")

    sum_result = reduce(
        lambda acc, val: acc + val,
        matrix[0] + matrix[1],
        0
    )
    return sum_result


result = sum_first_two_rows(matrix)
print(f"Сумма элементов первых двух строк: {result}")