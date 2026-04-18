#Из заданной строки отобразить только символы нижнего регистра. Использовать
#библиотеку string. Строка'In PyCharm, you can specify third-party standalone applications and
#run them as External Tools'.

import string
text = "In PyCharm, you can specify third-party standalone applications and run them as External Tools"

result = ""
for letter in text:
    if 'a' <= letter <= 'z':
        result += letter

print(result)