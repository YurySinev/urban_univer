class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color, *sides):
        self.__color = [255, 255, 255]
        if len(color) == 3:
            r, g, b = color  # распаковываем кортеж
            self.set_color(r, g, b)  # передаем его на проверку и установку
        if self.__color != [255, 255, 255]:
            self.filled = True
        self.__sides = [1 for i in range(self.sides_count)]  # список с единицами по количеству сторон

    def __str__(self):
        return '_____Просто фигура_____'

    def __is_valid_sides(self, *sides):  # служебный, принимает неограниченное кол-во сторон,
        # возвращает True если все стороны целые положительные числа и кол-во новых сторон
        # совпадает с текущим, False - во всех остальных случаях
        valid = []
        if len(sides) == self.__sides:
            valid.append(True)
        else:
            valid.append(False)
        for i in sides:
            if i <= 0 or not isinstance(i, int):
                valid.append(False)
                break
            else:
                continue
        if len(valid) == 1:
            valid.append(True)
        return valid

    def set_sides(self, *new_sides):  # должен принимать новые стороны, если их количество
        # не равно sides_count, то не изменять, в противном случае - менять
        if self.__is_valid_color(*new_sides):
            self.__sides = new_sides
        else:
            self.__sides = [1 for i in range(self.sides_count)]  # список с единицами по количеству сторон


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


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self.__radius = circumference / (2 * 3.14159)  # радиус

    def __str__(self):
        return '_____Окружность_____'

    def get_square(self):
        return 3.14159 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def __str__(self):
        return '_____Треугольник_____'

    def get_square(self) -> float:  # Площадь треугольника по формуле Герона
        a, b, c = self._Figure__sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        self.__sides = [1]
        super().__init__(color, *sides)

    def __str__(self):
        return '_____Кубик_____'

    def get_volume(self):
        return self._Figure__sides[0] ** 3

nums = 12, 13, 14, 15, 16, 17, 18
cube = Cube((123, 123, 125), 15, 14, -13)
print(cube._Figure__is_valid_sides(*nums))
print(cube._Cube__sides)
