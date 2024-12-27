# Домашнее задание по теме "Потоки на классах"
# Цель: научиться создавать классы наследованные от класса Thread.
# Задача "За честь и отвагу!"

import threading
import time

class KnightThread(threading.Thread):
    """ Класс, запускающий в потоке класс рыцаря.
    """
    def __init__(self, knight, delay):
        super().__init__()
        self.knight = knight
        self.delay = delay

    def run(self):
        time.sleep(self.delay)
        self.knight.fight()

class Knight:
    """ Класс рыцаря. Атрибуты: name и power (количество врагов, которые рыцарь может
    убить за день). Метод fight() - битва против 100 врагов.
    """
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def fight(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies:
            time.sleep(1)
            enemies -= self.power
            days += 1
            print(f'{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

# Создание объектов рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Создание и запуск потоков для каждого рыцаря с задержкой для второго
thread_first_knight = KnightThread(first_knight, 0)
thread_second_knight = KnightThread(second_knight, 1)

thread_first_knight.start()
thread_second_knight.start()
thread_first_knight.join()
thread_second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')