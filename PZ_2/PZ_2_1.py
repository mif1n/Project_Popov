
number = int(input("Введите трехзначное число: "))
if 100 <= number <= 999:
    hundreds = number // 100  # получаем сотни
    tens = (number // 10) % 10  # получаем десятки
    units = number % 10  # получаем единицы
    new_number = tens * 100 + hundreds * 10 + units
    print(f"Исходное число: {number}")
    print(f"Число после перестановки сотен и десятков: {new_number}")
else:
    print("Ошибка! Введите трехзначное число.")