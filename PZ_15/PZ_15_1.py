#Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации. БД
#должна содержать таблицу Нотариальные услуги со следующей структурой записи: ФИО
#клиента, услуга, сумма сделки, комиссионные (доход конторы).
import sqlite3 as sq

def main():
    try:
        with sq.connect('notary_office.db') as con:
            cur = con.cursor()

            # Удаляем таблицу при каждом запуске, чтобы гарантировать правильную структуру
            cur.execute("DROP TABLE IF EXISTS notary_services")

            # 1. Создание таблицы (Вариант 20: Нотариальная контора)
            cur.execute("""CREATE TABLE IF NOT EXISTS notary_services(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_fio TEXT NOT NULL,
                service TEXT NOT NULL,
                deal_sum REAL NOT NULL,
                commission REAL NOT NULL
            )""")

            # 2. Ввод 10 записей в БД
            records = [
                ('Иванов И.И.', 'Оформление наследства', 50000.0, 5000.0),
                ('Петрова А.С.', 'Договор купли-продажи', 120000.0, 8500.0),
                ('Сидоров В.В.', 'Юридическая консультация', 5000.0, 1500.0),
                ('Кузнецов Д.Д.', 'Выдача доверенности', 8000.0, 2000.0),
                ('Морозова Е.Е.', 'Договор аренды', 25000.0, 3500.0),
                ('Волков К.К.', 'Регистрация недвижимости', 200000.0, 15000.0),
                ('Лебедева М.М.', 'Заверение копий', 7000.0, 1800.0),
                ('Новиков Р.Р.', 'Семейное соглашение', 45000.0, 4000.0),
                ('Орлов Т.Т.', 'Договор займа', 30000.0, 3000.0),
                ('Соколов П.П.', 'Оформление завещания', 60000.0, 6000.0)
            ]
            cur.executemany(
                "INSERT INTO notary_services(client_fio, service, deal_sum, commission) VALUES(?, ?, ?, ?)",
                records
            )

            # 3. Поиск (3 запроса с условиями)
            print("=== ПОИСК ===")
            print("1. Услуги с комиссией более 4000 руб:")
            cur.execute("SELECT client_fio, service, deal_sum, commission FROM notary_services WHERE commission > 4000")
            for row in cur:
                print(row)

            print("\n2. Услуги, содержащие слово 'Договор':")
            cur.execute("SELECT * FROM notary_services WHERE service LIKE '%Договор%'")
            for row in cur:
                print(row)

            print("\n3. Сделки от 20000 до 100000 руб. (сортировка по ФИО):")
            cur.execute("SELECT * FROM notary_services WHERE deal_sum BETWEEN 20000 AND 100000 ORDER BY client_fio")
            for row in cur:
                print(row)

            # 4. Редактирование (3 запроса)
            print("\n=== РЕДАКТИРОВАНИЕ ===")
            cur.execute("UPDATE notary_services SET commission = commission * 1.1 WHERE deal_sum > 80000")
            print("1. Комиссия увеличена на 10% для сделок > 80000")

            cur.execute("UPDATE notary_services SET service = 'Срочное оформление' WHERE client_fio LIKE 'П%'")
            print("2. Услуга изменена для клиентов на букву 'П'")

            cur.execute("UPDATE notary_services SET deal_sum = deal_sum - 2000 WHERE commission < 2500")
            print("3. Сумма сделки уменьшена на 2000 при комиссии < 2500")

            # 5. Удаление (3 запроса)
            print("\n=== УДАЛЕНИЕ ===")
            cur.execute("DELETE FROM notary_services WHERE deal_sum < 10000")
            print("1. Удалены записи с суммой сделки < 10000")

            cur.execute("DELETE FROM notary_services WHERE service = 'Юридическая консультация'")
            print("2. Удалена услуга 'Юридическая консультация'")

            cur.execute("DELETE FROM notary_services WHERE client_fio IN ('Кузнецов Д.Д.', 'Лебедева М.М.')")
            print("3. Удалены записи указанных клиентов")

            # Проверка итогового состояния
            print("\n=== ИТОГОВАЯ ТАБЛИЦА ===")
            cur.execute("SELECT * FROM notary_services")
            for row in cur:
                print(row)

    except sq.Error as e:
        print(f"Ошибка работы с базой данных: {e}")

if __name__ == "__main__":
    main()