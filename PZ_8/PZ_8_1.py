# Подсчитайте сумму значений в словаре. d = {'a':100, 'b':200}.
# Часть 1: Считаем сумму в готовом словаре
print("Исходный словарь:", {'a': 100, 'b': 200})
print("Сумма:", 100 + 200)

print("\n" + "-" * 20)

import random

new_dict = {}
try:
    n = int(input("Сколько чисел добавить? "))

    for i in range(n):
        key = chr(random.randint(97, 122))

        while True:
            try:
                value = int(input(f"Число для '{key}': "))
                break
            except:
                print("Нужно число!")

        new_dict[key] = value

    print("\nПолучился словарь:", new_dict)
    print("Сумма чисел:", sum(new_dict.values()))

except:
    print("Что-то пошло не так")