"""Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        count = ''
        for i in self.matrix:
            for j in i:
                count += f'{j}\t'
            count += f'\n'
        return count

    def __add__(self, other):
        matrix_list = []
        for i in range(len(self.matrix)):
            matrix_list.append([])
            for j in range(len(self.matrix[0])):
                matrix_list[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(matrix_list)


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_3 = Matrix([[3, 5, 8], [8, 3, 7]])

print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_1 + matrix_2)
