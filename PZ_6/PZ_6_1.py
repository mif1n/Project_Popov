# Дан список размера N и целые числа K и L (1 < K < L < N). Найти среднее
# арифметическое элементов список с номерами от K до L включительно.
import random

N = int(input("Введите размер списка N: "))

numbers = [random.randint(1, 100) for _ in range(N)]

K = int(input("Введите K: "))
L = int(input("Введите L: "))

if not (1 < K < L < N):
    print("Ошибка: должно быть 1 < K < L < N")
else:
    selected = numbers[K - 1:L]

    average = sum(selected) / len(selected)

    print(f"\nСлучайный список: {numbers}")
    print(f"Элементы с {K} по {L}: {selected}")
    print(f"Среднее арифметическое: {average:.2f}")