#Вариант 20. Дано трехзначное число. Вывести число, полученное при
# перестановке цифр сотен и десятков исходного числа (например, 123 перейдет в 213)

try:
    number = int(input("Введите трехзначное число: "))
    if 100 <= number <= 999:
        num_str = str(number)

        result = int(num_str[1] + num_str[0] + num_str[2])

        print(f"{number} -> {result}")
    else:
        print("Ошибка: число должно быть от 100 до 999")
except ValueError:
    print("Ошибка: введите целое число")
except Exception as e:
    print(f"Произошла ошибка: {e}")