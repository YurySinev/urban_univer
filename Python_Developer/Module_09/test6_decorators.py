# пример 1 - создание простого декоратора:
import time

# def null_decorator(func):
#     return func
#
# def greet():
#     return 'Hello!'
#
# greet = null_decorator(greet)
# print(greet())

print()
# пример 2 - можно использовать @ для декорирования функции за один шаг:
print()


def null_decorator(func):
    print('Я тут - декоратор')
    return func


@null_decorator
def greet():
    return "Hello!"


print(greet())

print()


# пример 3 - почему нужно внутри декоратора определить еще одну функцию:

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


# @uppercase
def greet_2():
    return 'Hello!'


greet_dec = uppercase(greet_2)
print(greet_2())  # обычный вызов. Возможно, если нет @uppercase
print(greet_dec())  # вызов с докоратором

print()
# пример 4 - практическое использование декоратора:

import sys


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f"Функция работала {elapsed} секунд(ы).")
        return result

    return surrogate

@time_track
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


sys.set_int_max_str_digits(100000)

result = digits(3141, 5926, 2718, 2818)
print(result)
