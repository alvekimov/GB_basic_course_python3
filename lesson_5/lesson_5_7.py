import json

with open('text_7.txt', 'r', encoding='utf-8') as f:
    dict_profit = {}
    average_profit = {}
    for line in f:
        profit = int(line.split()[2]) - int(line.split()[3])
        dict_profit[line.split()[0]] = profit
    list_profit = [val for val in dict_profit.values() if val > 0]

    average_profit['average_profit'] = sum(list_profit) / len(list_profit)
    list = [dict_profit, average_profit]

with open('text_7_new.json', 'w', encoding='utf-8') as func:
    json.dump(list, func, ensure_ascii=False, indent=4)

