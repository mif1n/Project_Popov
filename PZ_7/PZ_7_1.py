# Дано целое положительное число. Вывести символы, изображающие цифры этого
# числа (в порядке слева направо).
def textp(sentence):
    words = sentence.split()
    result = []

    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)

    return " ".join(result)

text = input("Введите строку: ")

result = textp(text)
print("Результат:", result)