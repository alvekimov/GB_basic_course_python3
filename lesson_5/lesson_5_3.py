with open('text_3.txt', 'r', encoding='utf-8') as f:
    dict = {}
    for line in f:
        dict[line.split()[0]] = line.split()[1]
    print(f'Оклад менее 20т.р. имеют: ')
    all_salary = 0
    for key, val in dict.items():
        if float(val) < 20000:
            print(f'\t{key} - {val} руб')
        all_salary += float(val)
    print(f'Средняя заработная плата по списку составлят: {all_salary / len(dict)} руб.')
