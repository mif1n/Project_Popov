#Даны два числа. Вывести вначале большее, а затем меньшее из них.
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if num1 >= num2:
        larger, smaller = num1, num2
    else:
        larger, smaller = num2, num1

    print(f"{larger} {smaller}")

except ValueError:
    print("Ошибка: необходимо вводить числа")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")