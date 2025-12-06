# Дан целочисленный список размера N. Найти максимальное количество его
# одинаковых элементов.
numbers = [1, 3, 2, 3, 4, 3, 2, 2, 2, 5]
max_count = max(numbers.count(x) for x in set(numbers))
print(f"Список: {numbers}")
print(f"Максимальное количество одинаковых: {max_count}")