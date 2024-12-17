# Домашнее задание по теме "Итераторы"

# Задача "Range - это просто"
class StepValueError(ValueError):
    def __init__(self, message="Шаг указан неверно"):
        self.message = message


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start  # start - целое число, с которого начинается итерация.
        self.stop = stop  # stop - целое число, на котором заканчивается итерация.
        if step == 0:  # проверяется step на равенство 0
            raise StepValueError('Шаг не может быть равен 0')
        else:
            self.step = step  # step - шаг, с которым совершается итерация.
        # self.pointer = start  # pointer - указывает на текущее число в итерации (изначально start)

    # Методы:

    def __iter__(self):  # сбрасывает значение pointer на start и возвращает сам объект итератора.
        self.pointer = self.start
        return self

    def __next__(self):
        def moving_up():  # движение вверх от start к stop
            if self.pointer > self.stop:
                raise StopIteration
            else:
                current_value = self.pointer
                self.pointer += self.step
                return current_value

        def moving_down():  # движение вниз от start к stop
            if self.pointer < self.stop:
                raise StopIteration
            else:
                current_value = self.pointer
                self.pointer += self.step
                return current_value

        # Выбор направления итерации:
        if self.start < self.stop and self.step > 0:  # при этих условиях
            return moving_up()  # движемся вверх
        elif self.start > self.stop and self.step < 0:  # при этих условиях
            return moving_down()  # движемся вниз
        else:  # при иных условиях
            raise StopIteration  # никуда не движемся


if __name__ == '__main__':
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

    for i in iter2:
        print(i, end=' ')
    print()
    for i in iter3:
        print(i, end=' ')
    print()
    for i in iter4:
        print(i, end=' ')
    print()
    for i in iter5:
        print(i, end=' ')
    print()

# Вывод на консоль:
# Шаг указан неверно
# -5 -4 -3 -2 -1 0 1
# 6 8 10 12 14
# 5 4 3 2 1
