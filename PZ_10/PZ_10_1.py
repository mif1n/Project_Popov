#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:

#Исходные данные:
#Количество элементов:
#Минимальный элемент:
#Числа кратные трем:
#Количество чисел кратных трем:
# Создаем файл с числами
l = ['-10 3 9 4 -6 7 12 -15 8']

f1 = open('data_20_1.txt', 'w')
f1.writelines(l)
f1.close()

f2 = open('data_20_2.txt', 'w')
f2.write('Исходные данные:\n')
f2.writelines(l)
f2.close()

f1 = open('data_20_1.txt')
k = f1.read()
k = k.split()

for i in range(len(k)):
    k[i] = int(k[i])

f1.close()

min_el = k[0]
count_mult3 = 0
nums_mult3 = []

for i in range(len(k)):
    if k[i] < min_el:
        min_el = k[i]

    if k[i] % 3 == 0:
        nums_mult3.append(str(k[i]))
        count_mult3 += 1

f2 = open('data_20_2.txt', 'a')
f2.write('\n')
f2.write('Количество элементов: ' + str(len(k)) + '\n')
f2.write('Минимальный элемент: ' + str(min_el) + '\n')
f2.write('Числа кратные трем: ' + ' '.join(nums_mult3) + '\n')
f2.write('Количество чисел кратных трем: ' + str(count_mult3))
f2.close()