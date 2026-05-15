#Вариант 20  В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу


filename = "example.txt"
target = "Удаление строки"

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не существует")
    exit()

new_lines = []
for line in lines:
    stripped = line.rstrip('\n\r')
    if stripped == target and len(stripped) <= 1000:
        continue
    new_lines.append(line)

with open(filename, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)