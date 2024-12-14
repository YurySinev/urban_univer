# Домашнее задание по теме "Итераторы"

# Цель: освоить механизмы работы итераторов и описания методов __next__ и __iter__.
# Закрепить навык создания и выбрасывания исключений.

# Задача "Range - это просто":
# Создайте пользовательский класс исключения StepValueError, который наследуется от ValueError.
class StepValueError(ValueError):
    def __init__(self, message = "Шаг указан неверно"):
        self.message = message
    # Наследования достаточно, класс оставьте пустым при помощи оператора pass.
    # pass

# Создайте класс Iterator, который обладает следующими свойствами:
class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start  # start - целое число, с которого начинается итерация.
        self.stop = stop    # stop - целое число, на котором заканчивается итерация.
        if step == 0:       # проверяется step на равенство 0
            raise StepValueError('Шаг не может быть равен 0')
        else:
            self.step = step    # step - шаг, с которым совершается итерация.
        self.pointer = start    # pointer - указывает на текущее число в итерации (изначально start)

# Методы:

    def __iter__(self):  # метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
        pass
    def __next__(self): # метод, увеличивающий атрибут pointer на step. В зависимости от знака атрибута step итерация
        # завершится либо когда pointer станет больше stop, либо меньше stop. Учтите это при описании метода.
        pass


# Пример результата выполнения программы:

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


# for i in iter2:
#     print(i, end=' ')
#     print()
# for i in iter3:
#     print(i, end=' ')
#     print()
# for i in iter4:
#     print(i, end=' ')
#     print()
# for i in iter5:
#     print(i, end=' ')
#     print()

# Вывод на консоль:
# Шаг указан неверно
# -5 -4 -3 -2 -1 0 1
# 6 8 10 12 14
# 5 4 3 2 1

# Примечания:
# Особое внимание уделите методу __next__ и условиям в нём.
