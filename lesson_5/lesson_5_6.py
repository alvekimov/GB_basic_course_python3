with open('text_6.txt', 'r', encoding='utf-8') as f:
    dict = {}
    for line in f:
        line = line.replace('-', '0').replace(':', '').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '')
        dict[line.split()[0]] = sum(map(int, line.split()[1:]))
    print(dict)
