# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Задача "Потоки гостей в кафе":
# Необходимо имитировать ситуацию с посещением гостями кафе.

import random
import threading
import queue
import time


#
class Table:
    """ 1. Объекты этого класса должны создаваться следующим способом - Table(1)
    2. Обладать атрибутами number - номер стола
    и guest - гость, который сидит за этим столом (по умолчанию None) """

    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    """ 1. Должен наследоваться от класса Thread (быть потоком).
    2. Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
    3. Обладать атрибутом name - имя гостя.
    4. Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд."""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        time.sleep(random.randint(3, 10))


class Cafe:
    """ 1. Объекты этого класса должны создаваться так: Cafe(Table(1), Table(2),....)
    2. Обладать атрибутами queue - очередь (объект класса Queue)
    и tables - столы в этом кафе (любая коллекция).
    3. Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
    """

    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):  # прибытие гостей
        # 1. Должен принимать неограниченное кол-во гостей (объектов класса Guest).
        for guest in guests:
            table_assigned = False
            for table in self.tables:
                # 2. Далее, если есть свободный стол, то сажать гостя за стол
                # (назначать столу guest), запускать поток гостя и выводить на экран строку
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest.start()
                    table_assigned = True
                    break
            # 3. Если же свободных столов для посадки не осталось, то помещать гостя
            # в очередь queue и выводить сообщение "<имя гостя> в очереди".
            if not table_assigned:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):  # метод имитирует процесс обслуживания гостей.
        # 1. Обслуживание пока очередь не пустая (метод empty) или хотя бы один стол занят:
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                # 2. Если за столом есть гость(поток) и гость(поток) закончил приём пищи
                # (поток завершил работу - метод is_alive),
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    table.guest = None  # стол освобождается
                    print(f'Стол номер {table.number} свободен')
                # 3. Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None),
                if not self.queue.empty() and table.guest is None:
                    new_guest = self.queue.get()  # получить имя гостя из очереди
                    table.guest = new_guest  # назначить ему стол
                    print(f'{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    new_guest.start()  # запустить поток этого гостя


if __name__ == '__main__':
    # Пример результата выполнения программы:
    # # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # # Имена гостей
    guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                    'Victoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
    # # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # # Заполнение кафе столами
    cafe = Cafe(*tables)
    # # Приём гостей
    cafe.guest_arrival(*guests)
    # # Обслуживание гостей
    cafe.discuss_guests()

# Вывод на консоль (последовательность может меняться из-за случайного времени прибывания гостя):
# Maria сел(-а) за стол номер 1
# Oleg сел(-а) за стол номер 2
# Vakhtang сел(-а) за стол номер 3
# Sergey сел(-а) за стол номер 4
# Darya сел(-а) за стол номер 5
# Arman в очереди
# Vitoria в очереди
# Nikita в очереди
# Galina в очереди
# Pavel в очереди
# Ilya в очереди
# Alexandra в очереди
# Oleg покушал(-а) и ушёл(ушла)
# Стол номер 2 свободен
# Arman вышел(-ла) из очереди и сел(-а) за стол номер 2
# .....
# Alexandra покушал(-а) и ушёл(ушла)
# Стол номер 4 свободен
# Pavel покушал(-а) и ушёл(ушла)
# Стол номер 3 свободен
