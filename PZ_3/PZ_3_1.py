#Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы
#одна пара взаимно противоположных».
def has_opposite_pair(numbers):

    try:
        return (numbers[0] == -numbers[1] or
                numbers[0] == -numbers[2] or
                numbers[1] == -numbers[2])
    except (IndexError, TypeError):
        return False

try:
    a = int(input("Введите первое целое число: "))
    b = int(input("Введите второе целое число: "))
    c = int(input("Введите третье целое число: "))

    numbers = [a, b, c]

    result = has_opposite_pair(numbers)

    print(f"Среди чисел {a}, {b}, {c} есть пара взаимно противоположных: {result}")

except ValueError:
    print("Ошибка: необходимо вводить целые числа")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")