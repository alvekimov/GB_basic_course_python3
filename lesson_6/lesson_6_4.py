from random import randint


class car:
    def __init__(self, name, max_speed, color, is_police):
        self.name = name
        self.color = color
        self.max_speed = max_speed
        self.is_police = is_police

    def go(self):
        print(f'The car {self.name} went.')

    def stop(self):
        print(f'The car {self.name} stop.\n')

    def turn(self, ):
        route = randint(0, 1)
        if route == 0:
            print(f'The car {self.name} turned left.')
        else:
            print(f'The car {self.name} turned right.')

    def show_speed(self):
        current_speed = randint(1, self.max_speed)
        print(f'Сurrent speed is {current_speed} km/h')


class town_car(car):
    def __init__(self, name, max_speed, color, is_police=False):
        super().__init__(name, max_speed, color, is_police)

    def show_speed(self):
        current_speed = randint(1, self.max_speed)
        if current_speed > 60:
            print(f'Overspeed for town_car!Overspeed!Overspeed!')
        print(f'Сurrent speed is {current_speed} km/h')


class work_car(car):
    def show_speed(self):
        current_speed = randint(1, self.max_speed)
        if current_speed > 40:
            print(f'Overspeed for work_car!Overspeed!Overspeed!')
        print(f'Сurrent speed is {current_speed} km/h')


class sportCar(car):
    def __init__(self, name, max_speed, color, is_police=False):
        super().__init__(name, max_speed, color, is_police)


class policeCar(car):
    def __init__(self, name, max_speed, color, is_police=True):
        super().__init__(name, max_speed, color, is_police)

    def go(self):
        print(f'The police car {self.name} went.')

    def stop(self):
        print(f'The police car {self.name} stop.\n')

    def turn(self):
        route = randint(0, 1)
        if route == 0:
            print(f'The police car {self.name} turned left.')
        else:
            print(f'The police car {self.name} turned right.')


car_1 = town_car('Ford', 170, 'blue')
car_1.go()
car_1.turn()
car_1.show_speed()
car_1.stop()

car_2 = sportCar('Lamborghini', 270, 'black')
car_2.go()
car_2.show_speed()
car_2.turn()
car_2.stop()

car_3 = policeCar('BMW', 250, 'black and white', True)
car_3.go()
car_3.show_speed()
car_3.turn()
car_3.stop()

car_4 = work_car('Opel', 150, 'yellow', False)
car_4.go()
car_4.show_speed()
car_4.turn()
car_4.stop()
