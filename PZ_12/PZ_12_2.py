#В матрице найти минимальный и максимальные элементы.

from functools import reduce

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def find_min_max(matrix):
    flat_list = reduce(lambda acc, row: acc + row, matrix, [])

    min_max = reduce(
        lambda acc, val: (min(acc[0], val), max(acc[1], val)),
        flat_list,
        (flat_list[0], flat_list[0])
    )

    return min_max


min_val, max_val = find_min_max(matrix)
print(f"Минимальный элемент: {min_val}")
print(f"Максимальный элемент: {max_val}")