with open('text_6.txt', 'r', encoding='utf-8') as f:
    dict = {}
    for line in f:
        line = line.replace('-', '0').replace(':', '').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '')
        list_line = [i for i in line.split()]
        dict[list_line[0]] = sum(map(int, list_line[1:]))
    print(dict)
