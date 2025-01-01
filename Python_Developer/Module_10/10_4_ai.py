import threading
import queue
import random
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        # threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            table_assigned = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest.start()
                    table_assigned = True
                    break
            if not table_assigned:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    new_guest = self.queue.get()
                    table.guest = new_guest
                    print(f'{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    new_guest.start()

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