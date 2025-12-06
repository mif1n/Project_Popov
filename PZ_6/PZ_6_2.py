# Дан целочисленный список размера N. Найти максимальное количество его
# одинаковых элементов.
import random

try:
    N = int(input("Введите размер списка N: "))

    if N <= 0:
        print("Размер списка должен быть положительным!")
    else:
        numbers = [random.randint(1, 10) for _ in range(N)]

        max_count = max(numbers.count(x) for x in set(numbers))

        print(f"\nИсходный список: {numbers}")
        print(f"Размер списка N: {len(numbers)}")
        print(f"Максимальное количество одинаковых элементов: {max_count}")

except ValueError:
    print("Ошибка: введите целое число!")