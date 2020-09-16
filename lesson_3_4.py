# task 4

def func_pow(x, y):
    """"Программа принимает действительное положительное число x и целое отрицательное число y.
    Необходимо выполнить возведение числа x в степень y"""
    x_in_pow_y = 1
    for i in range(abs(round(y))):
        x_in_pow_y = x_in_pow_y * abs(x)
    return round((1 / x_in_pow_y), 5)


print(func_pow(21, -3))
