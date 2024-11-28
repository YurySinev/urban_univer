# Домашнее задание по теме "Try и Except"

# Задание "Программистам всё можно":

# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float),
# так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать
# строковое представление этих двух данных вместе (в том же порядке). Во всех остальных
# случаях выполнять стандартные действия.

def add_everything_up(a, b):
    try:
        return round(a + b, 3)
    except TypeError as err:
        return str(a) + str(b)
    except NameError as err:
        print(f'Непонятная ошибка {err}')
    else:
        ...
    finally:
        ...


# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('T-', [34, 65]))
print(add_everything_up({1: 2, 3: 4, 5: 6}, (7, 8, 9, 10)))

# Вывод в консоль:
# 123.456строка
# яблоко4215
# 130.456
