# Домашнее задание по теме "Потоки на классах"
# Цель: научиться создавать классы наследованные от класса Thread.
# Задача "За честь и отвагу!":

import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name  # Атрибут name - имя рыцаря. (str)
        self.power = power  # Атрибут power - сила рыцаря. (int)

    # А также метод run, в котором рыцарь будет сражаться с врагами:
    def run(self) -> None:
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies:
            time.sleep(1)
            enemies -= self.power
            days += 1
            print(f'{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


# Пример результата выполнения программы:
if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    # Запуск потоков и остановка текущего
    first_knight.start()
    time.sleep(1)
    second_knight.start()
    first_knight.join()
    second_knight.join()

    # Вывод строки об окончании сражения
    print('Все битвы закончились!')

# Вывод на консоль:
# Sir Lancelot, на нас напали!
# Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.
# Sir Galahad, на нас напали!
# Sir Galahad, сражается 1 день(дня)..., осталось 80 воинов.
# Sir Galahad, сражается 2 день(дня)..., осталось 60 воинов.
# Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов.
# Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов.
# Sir Galahad, сражается 3 день(дня)..., осталось 40 воинов.
# Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов.
# Sir Galahad, сражается 4 день(дня)..., осталось 20 воинов.
# Sir Galahad, сражается 5 день(дня)..., осталось 0 воинов.
# Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов.
# Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов.
# Sir Galahad одержал победу спустя 5 дней(дня)!
# Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов.
# Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов.
# Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов.
# Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов.
# Sir Lancelot одержал победу спустя 10 дней(дня)!
# Все битвы закончились!
