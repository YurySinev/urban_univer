from module_10_4 import *

# # Создание столов
tables = [Table(number) for number in range(1, 6)]
# # Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Victoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# # Создание гостей
guests = [Guest(name) for name in guests_names]
for i in guests:
    i.start()
    i.join()