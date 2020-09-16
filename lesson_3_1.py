# task 1

def func_div(a, b):
    """Функция деления с исклчением деления на ноль"""
    try:
        return a / b
    except ZeroDivisionError:
        return 'Error. Division by zero'


print(func_div(int(input('First number: ')), int(input('Second number: '))))
