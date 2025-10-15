def has_opposite_pair(numbers):
    try:
        # Проверяем, что передано ровно 3 числа
        if len(numbers) != 3:
            raise ValueError("Функция принимает ровно 3 числа")

        # Проверяем, что все элементы являются целыми числами
        if not all(isinstance(num, int) for num in numbers):
            raise TypeError("Все элементы должны быть целыми числами")

        # Проверяем все возможные пары чисел
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                # Числа взаимно противоположны, если их сумма равна 0
                if numbers[i] + numbers[j] == 0:
                    return True

        # Если ни одна пара не найдена
        return False

    except (ValueError, TypeError) as e:
        print(f"Ошибка: {e}")
        return False


def main():

    try:
        # Примеры для тестирования
        test_cases = [
            [1, 2, 3],  # Нет противоположных пар
            [1, -1, 3],  # Есть пара (1, -1)
            [5, -5, 0],  # Есть пара (5, -5)
            [2, -3, -2],  # Есть пара (2, -2)
            [-1, 1, 1],  # Есть пара (-1, 1)
            [0, 0, 1]  # Есть пара (0, 0) - ноль противоположен сам себе
        ]

        print("Проверка наличия взаимно противоположных пар в числах:")
        print("-" * 50)

        for i, numbers in enumerate(test_cases, 1):
            result = has_opposite_pair(numbers)
            print(f"Тест {i}: {numbers} -> {result}")

    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


# Точка входа в программу
if __name__ == "__main__":
    main()