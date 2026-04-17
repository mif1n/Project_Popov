#Из заданной строки отобразить только символы нижнего регистра. Использовать
#библиотеку string. Строка'In PyCharm, you can specify third-party standalone applications and
#run them as External Tools'.
import string

# Заданная строка
text = "In PyCharm, you can specify third-party standalone applications and run them as External Tools"

# Фильтрация: оставляем только символы нижнего регистра из английского алфавита
lowercase_chars = filter(lambda c: c in string.ascii_lowercase, text)

# Объединяем в строку и выводим
print(''.join(lowercase_chars))