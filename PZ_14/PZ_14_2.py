# Вариант 20   Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 1 – 9.


filename = "text.txt"
target = "Удаляемая строка"

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("Файл не найден")
    exit()

with open(filename, 'w', encoding='utf-8') as f:
    for line in lines:
        if line.rstrip('\n\r') == target:
            if '(' in line or ')' in line or '[' in line or ']' in line or '{' in line or '}' in line or '"' in line or "'" in line:
                continue
        f.write(line)