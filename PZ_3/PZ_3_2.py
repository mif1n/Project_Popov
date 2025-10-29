#Даны два числа. Вывести вначале большее, а затем меньшее из них.
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    print(f"{max(num1, num2)} {min(num1, num2)}")

except ValueError:
    print("Ошибка: необходимо вводить числа")