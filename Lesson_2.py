# task 1

my_list = [1, '2', True, 4, 5, [0, 1], (0, 1), {1, 2, 3}, {1: True, 2: False}]
print(my_list)
for i in range(len(my_list)):
    print(f'type for {my_list[i]} - {type(my_list[i])}')

# task 2

start_list = [int(i) for i in input('Enter numbers with space: ').split()]
result_list = start_list.copy()
for i in range(1, len(start_list), 2):
    result_list[i] = start_list[i - 1]
    result_list[i - 1] = start_list[i]
print(f'Your start list - {start_list}, result list - {result_list}')

# task 3

# first version task 3
winter_months = ['12', '1', '2']
spring_months = ['3', '4', '5']
summer_months = ['6', '7', '8']

enter_number_month = input('Enter number months: ')
if not enter_number_month.isdigit() or not 0 < int(enter_number_month) < 12:
    print('Your enter not number or not right number.')
else:
    if enter_number_month in winter_months:
        print('Your enter winter month.')
    elif enter_number_month in spring_months:
        print('Your enter spring month.')
    elif enter_number_month in summer_months:
        print('Your enter summer month.')
    else:
        print('Your enter months are autumn.')

# second version task 3
dict = {
    'winter_months': ['12', '1', '2'],
    'spring_months': ['3', '4', '5'],
    'summer_months': ['6', '7', '8']
}

enter_number_month = input('Enter number months: ')
if not enter_number_month.isdigit() or not 0 < int(enter_number_month) < 12:
    print('Your enter not number or not right number.')
else:
    if enter_number_month in dict['winter_months']:
        print('Your enter winter month.')
    elif enter_number_month in dict['spring_months']:
        print('Your enter spring month.')
    elif enter_number_month in dict['summer_months']:
        print('Your enter summer month.')
    else:
        print('Your enter months are autumn.')

# task 4

enter_string = input('Enter string: ').split()
for i in enter_string:
    if len(i) < 11:
        print(i)
    else:
        print(i[:10])

# task 5

my_list = [7, 5, 3, 3, 2]
while True:
    ask_new_element = input('Do you want to enter an element? y | any simbol: ')
    if ask_new_element == 'y':
        new_element = int(input('Enter new element: '))
        for i in range(len(my_list)):
            if new_element > int(my_list[i]):
                my_list.insert(i, str(new_element))
                break
            elif new_element <= int(my_list[-1]):
                my_list.append(str(new_element))
                break
        print(my_list)
    else:
        break
# task 6

number_goods = int(input('How many goods do you want to enter? - '))
list_goods = []
for i in range(number_goods):
    name = input('Enter name goods: ')
    price = input('Enter price goods: ')
    amount = input('Enter amount goods: ')
    unit = input('Enter unit goods: ')
    list_good = tuple([i + 1, {'name': name, 'price': price, 'amount': amount, 'unit': unit}])
    list_goods.append(list_good)
print('Общий список товаров:\n', list_goods)

analitics = {}
for good in list_goods:
    for key, value in good[1].items():
        if key in analitics:
            analitics[key].append(value)
        else:
            analitics[key] = [value]
print('Cписок аналитики:\n', analitics)
