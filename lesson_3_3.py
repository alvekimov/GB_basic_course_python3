# task 3

def my_func(a, b, c):
    """Функция вычисления суммы двух наибольших элементов из трех введенных"""
    list = [a, b, c]
    return (sum(list) - min(list))


print(my_func(a=int(input('First number: ')), b=int(input('Second number: ')), c=int(input('third number: '))))
