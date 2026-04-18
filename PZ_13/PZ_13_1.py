#Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
#«произведение».
import re


def extract_surnames(text):

    pattern = re.compile(r'\b([А-ЯЁ][а-яё-]+)\s+[А-ЯЁ]\.[А-ЯЁ]\.')
    surnames = pattern.findall(text)
    return surnames


def replace_words(text):

    pattern = re.compile(r'\bроман\b', re.IGNORECASE)
    new_text = pattern.sub('произведение', text)
    return new_text


def main():

    with open('writer.txt', 'r', encoding='utf-8') as file:
        text = file.read()


    surnames = extract_surnames(text)


    count = sum(1 for _ in surnames)

    print('Фамилии писателей:')
    for surname in surnames:
        print(surname)

    print(f'\nКоличество фамилий: {count}')

    new_text = replace_words(text)

    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(new_text)


if __name__ == '__main__':
    main()