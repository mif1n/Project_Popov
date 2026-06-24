#Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации. БД
#должна содержать таблицу Нотариальные услуги со следующей структурой записи: ФИО
#клиента, услуга, сумма сделки, комиссионные (доход конторы).
import sqlite3 as sq
from pz_15_data import NOTARY_RECORDS

def main():
    try:
        with sq.connect('notary_office.db') as con:
            cur = con.cursor()

            cur.execute("DROP TABLE IF EXISTS notary_services")
            cur.execute("""CREATE TABLE IF NOT EXISTS notary_services(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_fio TEXT NOT NULL,
                service TEXT NOT NULL,
                deal_sum REAL NOT NULL,
                commission REAL NOT NULL
            )""")

            cur.executemany(
                "INSERT INTO notary_services(client_fio, service, deal_sum, commission) VALUES(?, ?, ?, ?)",
                NOTARY_RECORDS
            )

            print("=== 1. ПОИСК ===")
            print("Услуги с комиссией более 4000 руб:")
            cur.execute("SELECT * FROM notary_services WHERE commission > 4000")
            for row in cur: print(row)

            print("\nУслуги, содержащие слово 'Договор':")
            cur.execute("SELECT * FROM notary_services WHERE service LIKE '%Договор%'")
            for row in cur: print(row)

            print("\nСделки от 20000 до 100000 руб. (сортировка по ФИО):")
            cur.execute("SELECT * FROM notary_services WHERE deal_sum BETWEEN 20000 AND 100000 ORDER BY client_fio")
            for row in cur: print(row)

            print("\n=== 2. РЕДАКТИРОВАНИЕ ===")
            cur.execute("UPDATE notary_services SET commission = commission * 1.1 WHERE deal_sum > 80000")
            print("1. Комиссия увеличена на 10% для сделок > 80000")

            cur.execute("UPDATE notary_services SET service = 'Срочное оформление' WHERE client_fio LIKE 'П%'")
            print("2. Услуга изменена для клиентов на букву 'П'")

            cur.execute("UPDATE notary_services SET deal_sum = deal_sum - 2000 WHERE commission < 2500")
            print("3. Сумма сделки уменьшена на 2000 при комиссии < 2500")

            print("\n=== 3. УДАЛЕНИЕ ===")
            cur.execute("DELETE FROM notary_services WHERE deal_sum < 10000")
            print("1. Удалены записи с суммой сделки < 10000")

            cur.execute("DELETE FROM notary_services WHERE service = 'Юридическая консультация'")
            print("2. Удалена услуга 'Юридическая консультация'")

            cur.execute("DELETE FROM notary_services WHERE client_fio IN ('Кузнецов Д.Д.', 'Лебедева М.М.')")
            print("3. Удалены записи указанных клиентов")

            print("\n=== ИТОГОВАЯ ТАБЛИЦА ===")
            cur.execute("SELECT * FROM notary_services")
            for row in cur: print(row)

    except sq.Error as e:
        print(f"Ошибка работы с базой данных: {e}")

if __name__ == "__main__":
    main()