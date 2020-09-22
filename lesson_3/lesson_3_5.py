# task 5

count = 0
stop = 1
print('If you want to out enter "q": ')
while stop:
    line_number = [i for i in input('Enter line number with space: ').split()]
    count_line = 0
    for i in line_number:
        if i == 'q':
            stop = 0
            break
        elif i.isdigit():
            count_line += int(i)
            count += int(i)
        else:
            continue
    print(f'Count line:{count_line}. (All count:{count})')
