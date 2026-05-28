#Вариант 20  В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу
from tkinter import *
from tkinter import ttk

def confirm_data():
    print("Данные подтверждены!")
    # Здесь можно добавить получение данных из полей
    print(f"Имя: {name_entry.get()}")
    print(f"Пароль: {password_entry.get()}")
    print(f"Возраст: {age_entry.get()}")
    print(f"Пол: {gender.get()}")
    print(f"Страна: {country_combo.get()}")
    print(f"Город: {city_combo.get()}")
    print(f"О себе: {about_text.get('1.0', END)}")

def cancel_data():
    """Обработчик кнопки отмены"""
    # Очистка всех полей
    name_entry.delete(0, END)
    password_entry.delete(0, END)
    age_entry.delete(0, END)
    country_combo.set('')
    city_combo.set('')
    about_text.delete('1.0', END)
    result_entry.delete(0, END)
    # Сброс чекбоксов
    music_var.set(0)
    video_var.set(0)
    drawing_var.set(0)
    print("Ввод отменен")

# Создание главного окна
root = Tk()
root.title("Форма регистрации пользователя")
root.geometry("600x650")

# Заголовок формы
title_label = Label(root, text="Форма регистрации пользователя", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Основной фрейм
main_frame = Frame(root, bd=2, relief="groove")
main_frame.pack(padx=20, pady=10, fill=BOTH, expand=True)

# Поле "Ваше имя"
name_frame = Frame(main_frame)
name_frame.pack(fill=X, padx=10, pady=5)
name_label = Label(name_frame, text="Ваше имя:", width=20, anchor="w")
name_label.pack(side=LEFT)
name_entry = Entry(name_frame, width=40)
name_entry.pack(side=LEFT, padx=10, fill=X, expand=True)

# Поле "Пароль"
password_frame = Frame(main_frame)
password_frame.pack(fill=X, padx=10, pady=5)
password_label = Label(password_frame, text="Пароль:", width=20, anchor="w")
password_label.pack(side=LEFT)
password_entry = Entry(password_frame, width=40, show="*")
password_entry.pack(side=LEFT, padx=10, fill=X, expand=True)

# Поле "Возраст"
age_frame = Frame(main_frame)
age_frame.pack(fill=X, padx=10, pady=5)
age_label = Label(age_frame, text="Возраст:", width=20, anchor="w")
age_label.pack(side=LEFT)
age_entry = Entry(age_frame, width=40)
age_entry.pack(side=LEFT, padx=10, fill=X, expand=True)

# Поле "Пол"
gender_frame = Frame(main_frame)
gender_frame.pack(fill=X, padx=10, pady=5)
gender_label = Label(gender_frame, text="Пол:", width=20, anchor="w")
gender_label.pack(side=LEFT)
gender = StringVar()
male_radio = Radiobutton(gender_frame, text="Мужской", variable=gender, value="male")
male_radio.pack(side=LEFT, padx=10)
female_radio = Radiobutton(gender_frame, text="Женский", variable=gender, value="female")
female_radio.pack(side=LEFT, padx=10)

# Поле "Ваши увлечения"
hobbies_frame = Frame(main_frame)
hobbies_frame.pack(fill=X, padx=10, pady=5)
hobbies_label = Label(hobbies_frame, text="Ваши увлечения:", width=20, anchor="w")
hobbies_label.pack(side=LEFT)
music_var = IntVar()
video_var = IntVar()
drawing_var = IntVar()
music_check = Checkbutton(hobbies_frame, text="Музыка", variable=music_var)
music_check.pack(side=LEFT, padx=5)
video_check = Checkbutton(hobbies_frame, text="Видео", variable=video_var)
video_check.pack(side=LEFT, padx=5)
drawing_check = Checkbutton(hobbies_frame, text="Рисование", variable=drawing_var)
drawing_check.pack(side=LEFT, padx=5)

# Поле "Ваша страна"
country_frame = Frame(main_frame)
country_frame.pack(fill=X, padx=10, pady=5)
country_label = Label(country_frame, text="Ваша страна:", width=20, anchor="w")
country_label.pack(side=LEFT)
country_combo = ttk.Combobox(country_frame, width=37, values=["Россия", "США", "Германия", "Франция", "Испания"])
country_combo.pack(side=LEFT, padx=10, fill=X, expand=True)

# Поле "Ваш город"
city_frame = Frame(main_frame)
city_frame.pack(fill=X, padx=10, pady=5)
city_label = Label(city_frame, text="Ваш город:", width=20, anchor="w")
city_label.pack(side=LEFT)
city_combo = ttk.Combobox(city_frame, width=37, values=["Москва", "Санкт-Петербург", "Нью-Йорк", "Берлин", "Париж"])
city_combo.pack(side=LEFT, padx=10, fill=X, expand=True)

# Поле "Кратко о себе"
about_frame = Frame(main_frame)
about_frame.pack(fill=X, padx=10, pady=5)
about_label = Label(about_frame, text="Кратко о себе:", width=20, anchor="w")
about_label.pack(side=LEFT)
about_text = Text(about_frame, width=40, height=3)
about_text.pack(side=LEFT, padx=10, fill=X, expand=True)
about_text.insert('1.0', "краткая информация о ваших увлечениях")

# Поле с математическим примером
math_frame = Frame(main_frame)
math_frame.pack(fill=X, padx=10, pady=10)
math_label = Label(math_frame, text="Решите пример, запишите результат в поле ниже:")
math_label.pack(anchor="w")

example_frame = Frame(math_frame)
example_frame.pack(fill=X, pady=5)
# Пример: 2 + 2 * 2 = 6
example_label = Label(example_frame, text="2 + 2 * 2 = ", font=("Arial", 12))
example_label.pack(side=LEFT)
result_entry = Entry(example_frame, width=10)
result_entry.pack(side=LEFT, padx=5)

# Кнопки
buttons_frame = Frame(main_frame)
buttons_frame.pack(pady=10)
cancel_button = Button(buttons_frame, text="Отменить ввод", command=cancel_data, width=20)
cancel_button.pack(side=LEFT, padx=10)
confirm_button = Button(buttons_frame, text="Данные подтверждаю", command=confirm_data, width=20)
confirm_button.pack(side=LEFT, padx=10)

# Запуск главного цикла
root.mainloop()