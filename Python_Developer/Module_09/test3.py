# Иногда нам нужны простые одноразовые функции, для которых def - слишком жирно.
# Для этого есть lambda.

############################
# пример 1 - lambda-функции
############################

my_func = lambda x: x + 10

print(my_func(42))
print(type(my_func))
print(my_func.__name__)

# введем lambda в функцию высшего порядка:
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# result = map(lambda x: x + 10, my_numbers)
# print(list(result))

######################################################################################
# пример 2 - lambda-функция может принимать как несколько параметров, так и ни одного:
######################################################################################

# my_numbers - уже есть
they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]


# result = map(lambda x, y: x + y, my_numbers, they_numbers)
# print(list(result))


# у лямбда-функции ограниченное применение.
# - Они создаются в процессе выполнения кода и из-за этого могут просадить быстродействия.
# - Они плохо сериализируются - могут быть проблемы в крупных фреймворках.
# - Не надо пытаться записать сложное выражение в лямбда-функцию: если там более 3-5 операторов - пора сделать «def».
#  (сериализация — это процесс перевода структуры данных в битовую последовательность)

################################################
# пример 3 - создание функций на лету, замыкания
################################################

def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2

    elif n == 3:
        def multiplier(x):
            return x * 3
    else:
        raise Exception("Я могу сделать умножение только на 2 или на 3")

    return multiplier


# by_2 = get_multiplier_v1(2)
# by_3 = get_multiplier_v1(3)
#
# result = map(by_2, my_numbers)
# print(list(result))
# print(list(map(get_multiplier_v1(3), they_numbers)))


# print(list(map(lambda x: x * 3, they_numbers)))     # такой же результат

##########
# пример 4
##########

def get_multiplier_v2(n):
    def multiplier(x):
        return x * n

    return multiplier


# by_10 = get_multiplier_v2(10)
# by_5 = get_multiplier_v2(5)
#
# # result = get_multiplier_v2(33)(55) # это работает! 1815
# # result = map(by_10, my_numbers)
# result = by_5(42)
# # print(list(result))
# print(result)

##############################################################################
# пример 5 - не стоит передавать в функцию высшего порядка изменяемые объекты:
##############################################################################

from pprint import pprint


def matrix(some_list):
    res = []

    def multiply_column(x):
        for element in some_list:
            res.append(element * x)
        return res

    return multiply_column


# matrix_on_my_numbers = matrix(my_numbers)
#
# result = map(matrix_on_my_numbers, they_numbers)
# print(list(result))


# my_numbers.extend([10, 20, 30])
# result = map(matrix_on_my_numbers, they_numbers)
# print(list(result))

#####################################################
# пример 6 - создание объекта, который можно вызвать:
#####################################################

class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        # если есть такой метод у класса, то его объект можно вызывать как функцию
        return x * self.n

# my_numbers
by_100500 = Multiplier(100500)

result = by_100500(42)
print(result)

result = map(by_100500, my_numbers)
pprint(list(result))

# Словарная сборка:
# Напишите словарную сборку для создания нового словаря, содержащего только пары ключ-значение,
# где значение больше 10, из словаря {'a': 5, 'b': 15, 'c': 20, 'd': 8}.

new_dic = {k: v for k, v in {'a': 5, 'b': 15, 'c': 20, 'd': 8}.items() if v > 10}
print(new_dic)
it = iter(new_dic)
