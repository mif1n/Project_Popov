#1.В последовательности на n целых элементов в первой ее половине найти
# количество положительных элементов.


n = int(input("Введите n: "))
numbers = list(map(int, input("Введите последовательность: ").split()))

# Вычисление первой половины и подсчёт положительных элементов
half = n // 2
positive_count = len(list(filter(lambda x: x > 0, numbers[:half])))

# Вывод результата
print(positive_count)