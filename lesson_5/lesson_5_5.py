from random import randint

with open('text_5.txt', 'w', encoding='utf-8') as f:
    try:
        n, start, end = int(input('Сколько чисел вы хотите: ')), int(input('Введите стартовое число: ')), \
                        int(input('Введите конечное число: '))
        if n <= 0:
            n = 'negative_number'
        for i in range(n):
            f.writelines(f'{randint(start, end)} ')
    except ValueError:
        print('Введены неверные значения!')
    except TypeError:
        print('Введены неверные значения!')

with open('text_5.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(f'Сумма чисел в файле равна {sum([int(i) for i in line.split()])}.')
