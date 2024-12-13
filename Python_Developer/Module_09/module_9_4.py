# Домашнее задание по теме "Создание функций на лету"
# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.
#
# Задача "Функциональное разнообразие":
import random

# from random import choice

# Lambda-функция:
# Даны 2 строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)):
print(list(map(lambda x, y: x == y, first, second)))


# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.

# Замыкание:
def get_advanced_writer(file_name):
    """
    Принимает название файла, в который встроенная функция write_everything
    построчно записывает неограниченное количество данных любого типа
    """

    def write_everything(*data_set):
        for line in data_set:
            try:
                with open(file_name, 'a') as file:
                    file.write(str(line) + '\n')
            except Exception:
                print("Непредвиденная ошибка")

    return write_everything


# Данный код:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Запишет данные в файл в таком виде:
# Это строчка
# ['А', 'это', 'уже', 'число', 5, 'в', 'списке']


# Метод __call__:
class MysticBall:
    """
    Объекты класса обладают атрибутом words, хранящим коллекцию строк.
    Метод __call__ случайным образом выбирает слово из words и возвращает его.
    """

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


# Ваш код (количество слов для случайного выбора может быть другое):
first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Вероятно', "Может быть", "Невозможно", "Вряд ли", "Исключено")
print(first_ball())
print(first_ball())
print(first_ball())

# Примерный результат (может отличаться из-за случайности выбора):
# Да
# Да
# Наверное
