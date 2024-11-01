# Дополнительное практическое задание по модулю: "Наследование классов."

class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color, *sides):
        self.__sides = [1 for i in range(self.sides_count)]  # список с единицами по количеству сторон
        self.__color = [255, 255, 255]
        if len(color) == 3:
            r, g, b = color  # распаковываем кортеж
            self.set_color(r, g, b)  # передаем его на проверку и установку
        if self.__color != [255, 255, 255]:
            self.filled = True

    def __is_valid_sides(self, *sides):  # служебный, принимает неограниченное кол-во сторон,
        # возвращает True если все стороны целые положительные числа и кол-во новых сторон
        # совпадает с текущим, False - во всех остальных случаях
        if len(sides) != self.sides_count:
            return False

    def set_sides(self, *new_sides):  # должен принимать новые стороны, если их количество
        # не равно sides_count, то не изменять, в противном случае - менять
        pass

    def get_sides(self):  # список размеров сторон фигуры
        return self.__sides

    def __is_valid_color(self, r, g, b) -> bool:  # проверка корректности RGB значений цвета
        for i in [r, g, b]:
            if i < 0 or i > 255:
                return False
            else:
                continue
        return True

    def set_color(self, r, g, b):  # сеттер атрибута __color
        if self.__is_valid_color(r, g, b):  # проверка корректности значений RGB
            self.__color = [r, g, b]

    def get_color(self):  # RGB цвет объекта
        return self.__color

    def __len__(self):  # периметр фигуры
        return sum(self.__sides)

    def __str__(self):
        return '_____Просто фигура_____'


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self.__radius = circumference / (2 * 3.14159)  # радиус

    def get_square(self):
        return 3.14159 * self.__radius ** 2

    def __str__(self):
        return '_____Окружность_____'


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self) -> float:  # Площадь треугольника по формуле Герона
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

    def get_volume(self):
        return self._Figure__sides[0] ** 3

    def __str__(self):
        return '_____Кубик_____'

    # Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    def get_volume(self):  # возвращает объём куба
        pass


if __name__ == '__main__':
    # Код для проверки:
    circle1 = Circle((200, 200, 100), 20)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    #
    # # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())
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
