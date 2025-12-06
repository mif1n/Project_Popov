# Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
# Составить функцию, которая будет находить на сколько квадратов можно разрезать
# данный прямоугольник, если от него каждый раз отрезать квадрат наибольшей площади.
def count_squares(a, b):
    squares = 0
    while a > 0 and b > 0:
        side = min(a, b)
        squares += 1
        if a > b:
            a -= side
        else:
            b -= side

    return squares
A = 10
B = 4

print(f"Прямоугольник: {A}x{B}")
result = count_squares(A, B)
print(f"Квадратов: {result}")
