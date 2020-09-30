class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'Bonus': self.bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Full name of person: {self.name} {self.surname}.'

    def get_total_income(self):
        try:
            return f'Income of {self.name} {self.surname} \
in position {self.position}: {sum(map(float, self._income.values())):.2f} rub.'
        except ValueError:
            return f'Error! Your enter error data. Wage and bonus are number.'


person_1 = Position('Alex', 'Petrov', 'cleaner', 1500.50, 1500)
print(person_1.get_full_name())
print(person_1.get_total_income())

person_2 = Position('Vasya', 'Alekseev', 'director', 4370, 370)
print(person_2.get_full_name())
print(person_2.get_total_income())

person_3 = Position('Test_name', 'Test_surname', 'Test_position', 'zgffc', 'chghgc')
print(person_3.get_full_name())
print(person_3.get_total_income())
