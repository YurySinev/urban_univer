class Animal:
    def __init__(self, name):
        self.alive = True  # живой
        self.fed = False  # сытый
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    def __init__(self, name):
        self.edible = False  # съедобный?
        self.name = name


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


if __name__ == '__main__':
    # Пример результата выполнения программы:
    # Выполняемый код(для проверки):
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)

## Вывод на консоль:
# Волк с Уолл-Стрит
# Цветик семицветик
# True
# False
# Волк с Уолл-Стрит не стал есть Цветик семицветик
# Хатико съел Заводной апельсин
# False
# True
