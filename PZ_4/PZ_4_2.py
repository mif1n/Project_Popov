#2. Дано целое число N (> 0). Найти сумму 1^1 + 2^2 + ... + N^N
try:
    n = int(input("N: "))

    if n > 0:
        total = 0
        i = 1
        while i <= n:
            total += i ** i
            i += 1

        print(f"Сумма: {total}")
    else:
        print("N > 0")

except ValueError:
    print("Ошибка: введите число")
except Exception as e:
    print(f"Ошибка: {e}")