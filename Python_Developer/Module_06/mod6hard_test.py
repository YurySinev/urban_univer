# from module6hard import Figura, Circle, Triangle, Cube
class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color, *sides):
        self.__sides = [i for i in sides]
        # self.__sides.append(*sides)
        self.__color = list(color)
        if self.__color != [255, 255, 255]:
            self.filled = True
        # self.filled = False

    def __str__(self):
        return '_____Просто фигура_____'


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        radius = circumference / (2 * 3.14159)  # вычисление радиуса
        self.__radius = radius

    def get_square(self):
        return 3.14159 * self.__radius ** 2

    def __str__(self):
        return '_____Окружность_____'


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):  # Площадь треугольника по формуле Герона
        a, b, c = self._Figure__sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area

    def __str__(self):
        return '_____Треугольник_____'


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        return self._Figure__sides[0] ** 2 * 6

    def __str__(self):
        return '_____Кубик Рубика(?)_____'


print()
circle1 = Circle((200, 200, 100), 12)
cube1 = Cube((222, 35, 130), 6, 4, 5)
fig = Figure((255, 255, 255), 11, 23, 43, 21, 33)
triangle = Triangle((233, 232, 231), 33, 44, 55)

# print(circle1)
print("Закрашен: ", circle1.filled)
print("Радиус:", circle1._Circle__radius)
print("Количество сторон: ", circle1.sides_count)
print("Список сторон: ", circle1._Figure__sides)
print("Цвет RGB:", circle1._Figure__color)
print("Площадь: ", circle1.get_square())
print()
#
print(cube1)
print("Закрашен: ", cube1.filled)
print("Радиус:", circle1._Circle__radius)
print("Количество сторон: ", cube1.sides_count)
print("Список сторон: ", cube1._Figure__sides)
print("Цвет RGB:", cube1._Figure__color)
print("Площадь: ", cube1.get_square())
print()
#
print(fig)
print("Количество сторон: ", fig.sides_count)
print("Список сторон: ", fig._Figure__sides)
print("Цвета: ", fig._Figure__color)
print("Закрашена: ", fig.filled)
print()
print(triangle)
print("Количество сторон: ", triangle.sides_count)
print("Список сторон: ", triangle._Figure__sides)
print("Цвета: ", triangle._Figure__color)
print("Закрашена: ", triangle.filled)
print("Площадь: ", triangle.get_square())
#
#
# Код для проверки:
# circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77)  # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15)  # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15)  # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())

# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
