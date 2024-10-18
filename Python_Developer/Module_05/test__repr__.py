class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Функция __repr__ возвращает вот это: ({self.x}, {self.y})'
    def __contains__(self, item):
        return item == self.x or item == self.y

# Создаем экземпляр класса Point
point = Point(3, 5)

# Выводим строковое представление объекта с помощью метода __repr__
print(repr(point))
print(point.__contains__(3))