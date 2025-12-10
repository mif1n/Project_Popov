# Дан список размера N, все элементы которого, кроме одного, упорядочены по
# убыванию. Сделать список упорядоченным, переместив элемент, нарушающий
# упорядоченность, на новую позицию.
import random

N = int(input("Введите размер списка N: "))
sorted_list = sorted([random.randint(1, 100) for _ in range(N)], reverse=True)

if N > 1:
    element = sorted_list.pop(random.randint(0, N-1))
    insert_pos = random.randint(1, N-2)
    sorted_list.insert(insert_pos, element)

print(f"\nИсходный список (с одним нарушением): {sorted_list}")

for i in range(1, len(sorted_list)):
    if sorted_list[i] > sorted_list[i-1]:
        wrong = sorted_list.pop(i)

        for j in range(len(sorted_list)):
            if wrong > sorted_list[j]:
                sorted_list.insert(j, wrong)
                break
        else:
            sorted_list.append(wrong)
        break

print(f"Исправленный список: {sorted_list}")