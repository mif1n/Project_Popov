# Дано целое положительное число. Вывести символы, изображающие цифры этого
# числа (в порядке слева направо).

import random

try:
    number = int(input("Введите целое положительное число: "))

    if number <= 0:
        print("Число должно быть положительным!")
    else:
        num_str = str(number)

        print(f"\nИсходное число: {number}")
        print("Цифры числа (слева направо):")
        for digit in num_str:
            print(digit)

except ValueError:
    print("Ошибка: введите целое число!")