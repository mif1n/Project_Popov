#1.В последовательности на n целых элементов в первой ее половине найти
# количество положительных элементов.

import random

n = int(input("Введите n: "))

numbers = [random.randint(-100, 100) for _ in range(n)]
print("Сгенерированная последовательность:", numbers)

half = n // 2
positive_count = len(list(filter(lambda x: x > 0, numbers[:half])))

print("Количество положительных в первой половине:", positive_count)