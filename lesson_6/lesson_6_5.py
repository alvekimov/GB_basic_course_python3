class stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(stationery):
    def draw(self):
        print(f'Запуск отрисовки "{self.title}".')


class Pencil(stationery):
    def draw(self):
        print(f'Запуск отрисовки "{self.title}".')


class Handle(stationery):
    def draw(self):
        print(f'Запуск отрисовки "{self.title}".')


stat_1 = Pen('Ручка')
stat_1.draw()
stat_2 = Pencil('Карандаш')
stat_2.draw()
stat_3 = Handle('Маркер')
stat_3.draw()
