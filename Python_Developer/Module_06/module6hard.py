# Дополнительное практическое задание по модулю: "Наследование классов."

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

    def get_color(self):  # возвращает список RGB цветов
        pass

    def __is_valid_color(self, r, g, b):  # служебный, принимает параметры r, g, b, который
        # проверяет корректность переданных значений перед установкой нового цвета.
        # Корректный цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно)
        pass

    def set_color(self):  # принимает параметры r, g, b - числа и изменяет атрибут __color
        # на соответствующие значения, предварительно проверив их на корректность. Если введены
        # некорректные данные, то цвет остаётся прежним.
        pass

    def __is_valid_sides(self):  # служебный, принимает неограниченное кол-во сторон,
        # возвращает True если все стороны целые положительные числа и кол-во новых сторон
        # совпадает с текущим, False - во всех остальных случаях
        pass

    def get_sides(self):  # должен возвращать значения атрибута __sides
        pass

    def __len__(self):  # должен возвращать периметр фигуры
        pass

    def set_sides(self, *new_sides):  # должен принимать новые стороны, если их количество
        # не равно sides_count, то не изменять, в противном случае - менять
        pass


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

    # Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    def get_volume(self):  # возвращает объём куба
        pass
