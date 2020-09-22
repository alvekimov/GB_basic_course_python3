# task 2

def person_data(**kwargs):
    print('Data person: ', end='')
    for key, val in kwargs.items():
        print(f'{key} - {val}', end=', ')


person_data(Name=input('Name: ').title(), Last_name=input('Last name: ').title(), Year_old=input('Year old: '),
            city=input('City: ').title(), email=input('Email: '), phone_number=input('Phone number: '))
