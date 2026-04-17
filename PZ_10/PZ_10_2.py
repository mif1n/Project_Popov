#Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
#количество символов в тексте. Сформировать новый файл, в который поместить строку
#наибольшей длины.
# Чтение файла и вывод содержимого
count_symbols = 0

for line in open('text18-20.txt', encoding='UTF-8'):
    print(line, end='')
    for s in line:
        count_symbols += 1

print('\nКоличество символов:', count_symbols)

# Поиск самой длинной строки
f1 = open('text18-20.txt', encoding='UTF-8')
lines = f1.readlines()
f1.close()

max_line = lines[0]

for i in range(len(lines)):
    if len(lines[i]) > len(max_line):
        max_line = lines[i]

# Запись в новый файл
f2 = open('text18-20_result.txt', 'w')
f2.write(max_line)
f2.close()