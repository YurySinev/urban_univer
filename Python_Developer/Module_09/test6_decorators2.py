# пример 1 - функция, которая возвращает декоратор

import time
import sys


def func_gen_dec(precision):
    print(f'получили точность, с которой надо выводить результат - {precision}')
    print('начинаем создавать декоратор')
    def dec(func):
        print(f'декоратор принял на вход функцию, которую надо отдекорировать - {func}')
        print('начинает создавать функцию-обертку')
        def wrapper(*args, **kwargs):
            print(f'мы - в функции-обертке, которая заместит реальную функцию - {func}')
            print('засекаем время')
            started_at = time.time()
            print('запускаем реальную функцию с переданными в функцию-обертку параметрами и запоминаем результат')
            result = func(*args, **kwargs)
            print('засекаем время окончания')
            ended_at = time.time()
            print('определяем затраченное время')
            elapsed = round(ended_at - started_at, precision)
            print('и выводим результат:')
            print(f"Функция работала {elapsed} секунд(ы).")
            return result
        print('декоратор создал функцию-обертку и возвращает ее')
        return wrapper
    print('декоратор создан, и пора его вернуть')
    return dec


# @func_gen_dec(precision=10)  # синтаксический сахар
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


sys.set_int_max_str_digits(10 ** 5)

# вариант без синтаксического сахара:
time_track_precision_6 = func_gen_dec(precision=8)  # вариант без синтаксического сахара
digits = time_track_precision_6(digits)  # вариант без синтаксического сахара
result = digits(3141, 5767, 2818)
print(result)
print()

# вариант с синтаксическим сахаром:
result1 = digits(4567, 9284, 2794, 1285)
print(result1)
