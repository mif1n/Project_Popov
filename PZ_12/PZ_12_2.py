# В матрице найти минимальный и максимальный элементы
import random
from functools import reduce

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = [[random.randint(-20, 30) for _ in range(cols)] for _ in range(rows)]

print("\nИсходная матрица:")
for row in matrix:
    print(row)

flat_list = [elem for row in matrix for elem in row]
filtered = list(filter(lambda x: isinstance(x, int), flat_list))
mapped = list(map(lambda x: x, filtered))

min_val = reduce(lambda a, b: a if a < b else b, mapped)
max_val = reduce(lambda a, b: a if a > b else b, mapped)

print(f"\nМинимальный элемент: {min_val}")
print(f"Максимальный элемент: {max_val}")