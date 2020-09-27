import time


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        while True:
            print(f'\033[31m{TrafficLight.__color[0]}')
            time.sleep(7)
            print(f'\033[33m{TrafficLight.__color[1]}')
            time.sleep(2)
            print(f'\033[32m{TrafficLight.__color[2]}')
            time.sleep(4)
            print(f'\033[33m{TrafficLight.__color[1]}')
            time.sleep(2)


TL = TrafficLight()
TL.running()
