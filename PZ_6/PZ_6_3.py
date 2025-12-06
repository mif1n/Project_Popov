# Дан список размера N, все элементы которого, кроме одного, упорядочены по
# убыванию. Сделать список упорядоченным, переместив элемент, нарушающий
# упорядоченность, на новую позицию.
lst = [10, 8, 7, 5, 9, 4, 3, 2, 1]

print(f"Исходный: {lst}")

for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        wrong = lst.pop(i)

        for j in range(len(lst)):
            if wrong > lst[j]:
                lst.insert(j, wrong)
                break
        break

print(f"Исправленный: {lst}")