class Horse:
    def __init__(self):
        self.x_distance = 0  # пройденный путь.
        self.sound = 'Frrr'  # звук, который издаёт лошадь.

    def run(self, dx):
        self.x_distance += dx  # изменение дистанции, увеличивает x_distance на dx.
        return self.x_distance


class Eagle:
    def __init__(self):
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл (отсылка)

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance  # изменение дистанции, увеличивает y_distance на dy.


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):  # где dx и dy изменения дистанции. В этом методе должны запускаться
        return self.run(dx), self.fly(dy)

    def get_pos(self):  # возвращает текущее положение пегаса в виде кортежа
        return self.x_distance, self.y_distance

    def voice(self):  # который печатает значение унаследованного атрибута sound.
        print(self.sound)



if __name__ == '__main__':
    # Пример результата выполнения программы:
    # Пример работы программы:
    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())
    #
    p1.voice()

# Вывод на консоль:
# (0, 0)
# (10, 15)
# (5, 35)
# I train, eat, sleep, and repeat
