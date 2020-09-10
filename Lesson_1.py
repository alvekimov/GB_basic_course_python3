# 1 task
print('\n1 task\n')
name = input('Enter your name: ')
age = int(input('Enter your age: '))
print(f'Hello, {name}! Are you really {age} age? How are you?!')

# 2 task
print('\n2 task\n')
time = int(input('Enter time in seconds: '))
hour = time // 3600
minutes = (time - hour * 3600) // 60
seconds = time % 60
print(f'Time: {hour:02d}:{minutes:02d}:{seconds:02d}')

# 3 task
print('\n3 task\n')
n = input('Enter number: ')
number = int(n) + int(n*2) + int(n*3)
print(f'Total number = {number}')


# 4 task
print('\n4 task\n')
n = input('Enter number: ')
i = 0
number = 0
while i < len(n):
    if int(n[i]) > number:
        number = int(n[i])
    i = i + 1
print(f'Max number: {number}')

# 5 task
print('\n5 task\n')
proceeds = int(input('Введите Выручку фирмы: '))
costs = int(input('Введите Издержки фирмы: '))

if proceeds > costs:
    print(f'Прибыль составила {proceeds - costs}')
    print(f'Рентабельность составила {(proceeds - costs) / proceeds:.2%}')
    number = int(input('Введите количество работников: '))
    print(f'Прибыль на одного сотрудника составила {(proceeds - costs) / number:.2f}')
elif proceeds < costs:
    print(f'Убыток составил {costs - proceeds}')
else:
    print('Выручка равна издержкам')

# 6 task
print('\n6 task\n')
a = int(input('Введите количество км в первый день: '))
b = int(input('Введите необходимую дистанцию: '))

i = 1
while True:
    a = a + a / 10
    i = i + 1
    if a > b:
        print(f'на {i}-й день спортсмен достиг результата — не менее {b} км.')
        break