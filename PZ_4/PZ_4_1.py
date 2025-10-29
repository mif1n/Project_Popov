#1. Дано вещественное число X и целое число N (> 0).
# Найти значение выражения 1 - X^2/(2!) + X^4/(4!) - ... + (-1)^N -X^2*N /((2-N)!) (N! = 12 ...N).
# Полученное число является приближенным значением функции cos в точке X.
try:
    x = float(input("X: "))
    n = int(input("N: "))

    if n > 0:
        total = 0
        i = 0
        while i <= n:
            # Вычисляем факториал (2*i)!
            factorial = 1
            j = 1
            while j <= 2 * i:
                factorial *= j
                j += 1

            # Вычисляем член ряда
            term = ((-1) ** i) * (x ** (2 * i)) / factorial
            total += term
            i += 1

        print(f"Результат: {total:.6f}")
    else:
        print("N > 0")

except:
    print("Ошибка ввода")