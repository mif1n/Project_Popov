# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 1 – 9.
from tkinter import *
from tkinter import ttk


def calculate_sets():
    # Получаем данные из текстового поля
    all_cars = {'bmv', 'merc', 'lada', 'vaz', 'opel', 'zig', 'tesla'}

    spain = {'bmv', 'lada', 'vaz'}
    honduras = {'merc', 'vaz', 'opel'}
    usa = {'zig', 'vaz'}

    # Операции с множествами
    all_countries = spain & honduras & usa  # Пересечение - во все страны
    some_countries = spain | honduras | usa  # Объединение - в некоторые страны
    not_exported = all_cars - some_countries  # Разность - не доставлены ни в одну

    # Очистка результата
    result_text.delete('1.0', END)

    # Вывод результатов
    result_text.insert(END, "=== РЕЗУЛЬТАТЫ ===\n\n")
    result_text.insert(END, f"Все марки машин: {all_cars}\n\n")
    result_text.insert(END, f"Завезены во ВСЕ страны:\n{all_countries}\n\n")
    result_text.insert(END, f"Завезены в НЕКОТОРЫЕ страны:\n{some_countries}\n\n")
    result_text.insert(END, f"НЕ завезены ни в одну страну:\n{not_exported}\n")


def clear_result():
    """Очистка результата"""
    result_text.delete('1.0', END)


# Создание главного окна
root = Tk()
root.title("Работа с множествами - марки машин")
root.geometry("700x500")

# Заголовок
title_label = Label(root, text="Экспорт марок машин в страны", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Основной фрейм
main_frame = Frame(root)
main_frame.pack(padx=20, pady=10, fill=BOTH, expand=True)

# Фрейм с исходными данными
data_frame = LabelFrame(main_frame, text="Исходные данные", padx=10, pady=10)
data_frame.pack(fill=X, pady=5)

cars_label = Label(data_frame, text="Все марки: {'bmv', 'merc', 'lada', 'vaz', 'opel', 'zig', 'tesla'}",
                   font=("Courier", 10))
cars_label.pack(anchor="w", pady=2)

spain_label = Label(data_frame, text="Spain: {'bmv', 'lada', 'vaz'}", font=("Courier", 10))
spain_label.pack(anchor="w", pady=2)

honduras_label = Label(data_frame, text="Honduras: {'merc', 'vaz', 'opel'}", font=("Courier", 10))
honduras_label.pack(anchor="w", pady=2)

usa_label = Label(data_frame, text="USA: {'zig', 'vaz'}", font=("Courier", 10))
usa_label.pack(anchor="w", pady=2)

# Фрейм с кнопками
buttons_frame = Frame(main_frame)
buttons_frame.pack(pady=10)

calc_button = Button(buttons_frame, text="Выполнить расчет", command=calculate_sets, width=20)
calc_button.pack(side=LEFT, padx=10)

clear_button = Button(buttons_frame, text="Очистить", command=clear_result, width=20)
clear_button.pack(side=LEFT, padx=10)

# Фрейм с результатом
result_frame = LabelFrame(main_frame, text="Результат", padx=10, pady=10)
result_frame.pack(fill=BOTH, expand=True, pady=5)

result_text = Text(result_frame, width=70, height=12, font=("Courier", 11))
result_text.pack(fill=BOTH, expand=True)

# Пояснение
info_label = Label(main_frame, text="Нажмите 'Выполнить расчет' для получения результатов",
                   fg="gray", font=("Arial", 9))
info_label.pack(pady=5)

# Запуск главного цикла
root.mainloop()