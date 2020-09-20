from sys import argv

# task 1

name, rate, output, prize = argv
try:
    salary = (float(rate) * float(output) + float(prize))
    print(f'Ставка в час равна: {rate} $/ч;\nВыработка в часах равна: {output} ч;\nПремия равна: {prize} $;')
    print(f'Заработная плата сотрудника составила: {salary:.2f} $.')
except ValueError:
    print('Введены неверные данные.')
