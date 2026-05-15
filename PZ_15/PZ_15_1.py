#Вариант 20
#Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации. БД
#должна содержать таблицу Нотариальные услуги со следующей структурой записи: ФИО
#клиента, услуга, сумма сделки, комиссионные (доход конторы).

import sqlite3 as sq

# Имя файла базы данных
DB_NAME = 'notary_office.db'

# Тестовые данные для заполнения: 10 позиций
# Структура: (ФИО клиента, услуга, сумма сделки, комиссионные)
INFO_SERVICES = [
    ("Иванов Иван Иванович", "Купля-продажа квартиры", 5_500_000.00, 25_000.00),
    ("Петров Петр Петрович", "Дарственная на дом", 3_200_000.00, 15_000.00),
    ("Сидорова Анна Сергеевна", "Оформление наследства", 1_200_000.00, 8_000.00),
    ("Козлов Дмитрий Алексеевич", "Заверение доверенности", 0.00, 1_500.00),
    ("Морозова Елена Валерьевна", "Брачный договор", 0.00, 3_000.00),
    ("Волков Андрей Николаевич", "Купля-продажа участка", 2_800_000.00, 18_000.00),
    ("Зайцева Ольга Дмитриевна", "Свидетельство о праве на наследство", 4_500_000.00, 22_000.00),
    ("Соколов Юрий Михайлович", "Согласие на выезд ребенка", 0.00, 1_200.00),
    ("Павлова Мария Игоревна", "Ипотечный договор", 7_800_000.00, 35_000.00),
    ("Новиков Александр Павлович", "Заверение копии документа", 0.00, 500.00),
]


def create_table():
    """Создание таблицы notary_services, если она не существует."""
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS notary_services (
                service_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_name TEXT NOT NULL,
                service_type TEXT NOT NULL,
                deal_amount REAL NOT NULL DEFAULT 0.0,
                commission REAL NOT NULL DEFAULT 0.0
            )
        """)


def fill_test_data():
    """Заполнение таблицы 10 тестовыми записями, если таблица пуста."""
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM notary_services")
        count = cur.fetchone()[0]

        if count == 0:
            # Используем executemany как в лекции (Раздаточный материал №12)
            cur.executemany(
                "INSERT INTO notary_services (client_name, service_type, deal_amount, commission) "
                "VALUES (?, ?, ?, ?)",
                INFO_SERVICES,
            )
            print(f"[INFO] Добавлено {len(INFO_SERVICES)} тестовых записей.")
        else:
            print(f"[INFO] В таблице уже есть {count} записей. Пропускаем автозаполнение.")


def print_all_records():
    """Вывод всех записей таблицы (SELECT *)."""
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM notary_services")
        # Используем cursor как итерируемый объект (Раздаточный материал №20)
        records = cur.fetchall()
        if not records:
            print("\n[INFO] Таблица пуста.")
            return
        print("\n--- Содержимое таблицы notary_services ---")
        print(f"{'ID':<5} {'ФИО клиента':<30} {'Услуга':<35} {'Сумма сделки':<15} {'Комиссия':<12}")
        print("-" * 100)
        for rec in records:
            print(f"{rec[0]:<5} {rec[1]:<30} {rec[2]:<35} {rec[3]:<15.2f} {rec[4]:<12.2f}")
        print("-" * 100)


# ---------- БЛОК ПОИСКА (3 варианта SQL-запросов) ----------

def search_by_client_name(substring):
    """
    Поиск №1: по подстроке в ФИО клиента (LIKE с шаблоном %).
    Условие: client_name LIKE '%substring%'.
    """
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM notary_services WHERE client_name LIKE ?",
            (f"%{substring}%",),
        )
        results = cur.fetchall()
        _print_search_results(results, f"Поиск по ФИО: '{substring}'")


def search_by_service_type(substring):
    """
    Поиск №2: по подстроке в названии услуги (LIKE с шаблоном %).
    Условие: service_type LIKE '%substring%'.
    """
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM notary_services WHERE service_type LIKE ?",
            (f"%{substring}%",),
        )
        results = cur.fetchall()
        _print_search_results(results, f"Поиск по услуге: '{substring}'")


def search_by_min_amount(min_amount):
    """
    Поиск №3: по сумме сделки (больше заданного значения).
    Условие: deal_amount > min_amount.
    """
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM notary_services WHERE deal_amount > ?",
            (min_amount,),
        )
        results = cur.fetchall()
        _print_search_results(results, f"Поиск: сумма сделки > {min_amount}")


# ---------- БЛОК УДАЛЕНИЯ (3 варианта SQL-запросов) ----------

def delete_by_exact_name(full_name):
    """
    Удаление №1: точное совпадение ФИО клиента.
    Условие: client_name = full_name.
    """
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(
            "DELETE FROM notary_services WHERE client_name = ?",
            (full_name,),
        )
        print(f"[DELETE] Удалено записей по клиенту '{full_name}': {cur.rowcount}")


def delete_by_service(service):
    """
    Удаление №2: точное совпадение названия услуги.
    Условие: service_type = service.
    """
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(
            "DELETE FROM notary_services WHERE service_type = ?",
            (service,),
        )
        print(f"[DELETE] Удалено записей по услуге '{service}': {cur.rowcount}")


def delete_by_min_commission(min_commission):
    """
    Удаление №3: удаление записей с комиссией МЕНЬШЕ заданного порога.
    Условие: commission < min_commission.
    """
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(
            "DELETE FROM notary_services WHERE commission < ?",
            (min_commission,),
        )
        print(f"[DELETE] Удалено записей с комиссией < {min_commission}: {cur.rowcount}")


# ---------- БЛОК РЕДАКТИРОВАНИЯ (3 варианта SQL-запросов) ----------

def update_client_name_by_id(record_id, new_name):
    """
    Редактирование №1: изменение ФИО клиента по ID записи.
    UPDATE ... SET client_name = new_name WHERE service_id = record_id.
    """
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(
            "UPDATE notary_services SET client_name = ? WHERE service_id = ?",
            (new_name, record_id),
        )
        if cur.rowcount > 0:
            print(f"[UPDATE] ФИО для записи ID={record_id} изменено на '{new_name}'.")
        else:
            print(f"[WARNING] Запись с ID={record_id} не найдена.")


def update_service_type_by_id(record_id, new_service):
    """
    Редактирование №2: изменение названия услуги по ID записи.
    UPDATE ... SET service_type = new_service WHERE service_id = record_id.
    """
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(
            "UPDATE notary_services SET service_type = ? WHERE service_id = ?",
            (new_service, record_id),
        )
        if cur.rowcount > 0:
            print(f"[UPDATE] Услуга для записи ID={record_id} изменена на '{new_service}'.")
        else:
            print(f"[WARNING] Запись с ID={record_id} не найдена.")


def increase_commission_by_percent(amount_threshold, percent):
    """
    Редактирование №3: увеличение комиссии на заданный процент
    для всех сделок, сумма которых превышает порог.
    Пример из лекции: UPDATE users SET score = score + 500 WHERE sex = 2.
    Здесь: UPDATE ... SET commission = commission * multiplier WHERE deal_amount > threshold.
    """
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        multiplier = 1 + (percent / 100.0)
        cur.execute(
            "UPDATE notary_services SET commission = commission * ? WHERE deal_amount > ?",
            (multiplier, amount_threshold),
        )
        print(
            f"[UPDATE] Комиссия увеличена на {percent}% "
            f"для сделок дороже {amount_threshold}. Затронуто строк: {cur.rowcount}"
        )


# ---------- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ----------

def _print_search_results(results, title):
    """Форматированный вывод результатов поиска."""
    print(f"\n--- {title} ---")
    if not results:
        print("Записей не найдено.")
        return
    for rec in results:
        print(
            f"ID: {rec[0]} | Клиент: {rec[1]} | Услуга: {rec[2]} | "
            f"Сумма: {rec[3]:.2f} | Комиссия: {rec[4]:.2f}"
        )


# ---------- ОСНОВНАЯ ПРОГРАММА ----------

def main():
    """Основная функция: демонстрация работы приложения."""
    print("========== ПРИЛОЖЕНИЕ «НОТАРИАЛЬНАЯ КОНТОРА» ==========")

    # 1. Подготовка БД и данных
    print("\n[1] Создание таблицы...")
    create_table()

    print("\n[2] Заполнение тестовыми данными (10 позиций)...")
    fill_test_data()

    # 2. Вывод исходного состояния
    print("\n[3] Исходное состояние таблицы:")
    print_all_records()

    # 3. Демонстрация ПОИСКА (3 запроса)
    print("\n[4] Демонстрация поиска (3 варианта):")
    search_by_client_name("Иван")
    search_by_service_type("Заверение")
    search_by_min_amount(5_000_000)

    # 4. Демонстрация РЕДАКТИРОВАНИЯ (3 запроса)
    print("\n[5] Демонстрация редактирования (3 варианта):")
    update_client_name_by_id(1, "Иванова Мария Сергеевна")
    update_service_type_by_id(5, "Расторжение брачного договора")
    increase_commission_by_percent(amount_threshold=3_000_000, percent=10)
    print_all_records()

    # 5. Демонстрация УДАЛЕНИЯ (3 запроса)
    print("\n[6] Демонстрация удаления (3 варианта):")
    delete_by_exact_name("Новиков Александр Павлович")
    delete_by_service("Согласие на выезд ребенка")
    delete_by_min_commission(1000.0)
    print_all_records()

    print("\n[INFO] Работа программы завершена.")


if __name__ == "__main__":
    main()