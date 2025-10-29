#Вариант 20. Дано трехзначное число. Вывести число, полученное при
# % // перестановке цифр сотен и десятков исходного числа (например, 123 перейдет в 213)
try:
    number = int(input("Введите трехзначное число: "))
    if 100 <= number <= 999:
        digit1 = number // 100  #(сотни)
        digit2 = (number // 10) % 10  #(десятки)
        digit3 = number % 10  #(единицы)

        result = digit2 * 100 + digit1 * 10 + digit3

        print(f"{number} -> {result}")
    else:
        print("Ошибка: число должно быть от 100 до 999")
except ValueError:
    print("Ошибка: введите целое число")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
