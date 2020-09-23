with open('text_1_2.txt', 'w', encoding='utf-8') as f:
    while True:
        enter = input('Enter data or press enter from quit: ')
        if enter == '':
            break
        f.writelines(f'{enter}\n')
print(f'You quit from enter\n')

with open('text_1_2.txt', 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        count += 1
        print(f'In line {count} - {len(line.split())} word(s).')
    print(f'Total number of lines are {count}')
