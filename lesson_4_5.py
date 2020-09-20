from functools import reduce

""" 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""


def mult(*args):
    count = 1
    for i in args:
        count *= int(i)
    return count


my_list = [i for i in range(100, 1001, 2)]
print(reduce(mult, my_list))
