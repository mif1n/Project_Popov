def display_numbers_in_order(num1, num2):
    try:
        # Проверяем, что оба аргумента являются числами
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Оба аргумента должны быть числами (int или float)")

        # Сравниваем числа и определяем большее и меньшее
        if num1 >= num2:
            larger = num1
            smaller = num2
        else:
            larger = num2
            smaller = num1

        # Выводим результат в требуемом порядке
        print(f"Большее число: {larger}")
        print(f"Меньшее число: {smaller}")

        return larger, smaller

    except TypeError as e:
        print(f"Ошибка типа данных: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None


def main():
    """
    Основная функция для демонстрации работы программы.
    """
    try:
        # Тестовые примеры
        test_cases = [
            (5, 3),  # Оба положительных
            (-2, -5),  # Оба отрицательных
            (7.5, 2.3),  # Дробные числа
            (0, -4),  # Ноль и отрицательное
            (10, 10),  # Равные числа
            (-3.2, 1.8),  # Отрицательное и положительное дробные
        ]

        print("Сравнение двух чисел:")
        print("=" * 40)

        for i, (a, b) in enumerate(test_cases, 1):
            print(f"\nТест {i}: числа {a} и {b}")
            print("-" * 20)
            result = display_numbers_in_order(a, b)

    except Exception as e:
        print(f"Ошибка в основной программе: {e}")


# Дополнительная функция для ручного ввода от пользователя
def user_input_mode():
    try:
        print("\n" + "=" * 50)
        print("Режим ручного ввода")
        print("=" * 50)

        # Получаем ввод от пользователя
        input1 = input("Введите первое число: ")
        input2 = input("Введите второе число: ")

        # Преобразуем в числа (пробуем сначала float, потом int)
        try:
            num1 = float(input1)
            num2 = float(input2)

            # Если числа целые, преобразуем к int для красивого вывода
            if num1.is_integer():
                num1 = int(num1)
            if num2.is_integer():
                num2 = int(num2)

        except ValueError:
            print("Ошибка: введите корректные числа!")
            return

        # Вызываем основную функцию
        display_numbers_in_order(num1, num2)

    except Exception as e:
        print(f"Ошибка в режиме ввода: {e}")


# Точка входа в программу
if __name__ == "__main__":
    # Запускаем тестовые примеры
    main()

    # Предлагаем пользователю ввести свои числа
    try:
        user_choice = input("\nХотите ввести свои числа? (да/нет): ").lower().strip()
        if user_choice in ['да', 'д', 'yes', 'y']:
            user_input_mode()
        else:
            print("Программа завершена.")
    except Exception as e:
        print(f"Ошибка при обработке выбора пользователя: {e}")