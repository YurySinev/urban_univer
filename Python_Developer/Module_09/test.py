def get_russian_names():
    return ['Вася', 'Петя', 'Коля']


######################################
# пример 1 - почему функция это объект
print(type(get_russian_names))
print(get_russian_names.__name__)

#################################################
# пример 2 - присвоение функции другой переменной:
my_func = get_russian_names
print(my_func())
print(my_func.__name__)


def get_british_names():
    return ['Oliver', 'Jack', 'Harry']


#############################################################
# пример 3 - с функцией можно работать как с обычным объектом:
name_getter = [get_russian_names, get_british_names]

for name_getter in name_getter:
    print(name_getter())


########################################################
# пример 4 - функции, принимающие на вход другие функции:
# иначе говоря, это - функции высшего порядка
def adder(args):
    res = 0
    for number in args:
        res += number
    return res


def multiplier(args):
    res = 1
    for number in args:
        res *= number
    return res


def process_numbers(numbers, function):
    result = function(numbers)
    print(f"Получилось: {result}")


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

process_numbers(my_numbers, adder)
process_numbers(numbers=my_numbers, function=multiplier)


#########################
# пример 5 - функция map:
# в Python есть встроенные функции высшего порядка, map - одна из них.
# Применяется к каждому элементу последовательности и формирует новый список результатов.

def mul_by_2(x):
    return x * 2


result = map(mul_by_2, my_numbers)
print(result)  # Вывод на консоль: <map object at 0x1027cff70>
# Почему? - map работает с "ленивыми" вычислениями
print(list(result))


###########################
# пример 6 - функция filter
# Вычисляет функцию для каждого элемента и добавляет элемент
# в список результатов только если функция вернёт True.

def is_odd(x):
    return x % 2

result = filter(is_odd, my_numbers)
print(result)
print(list(result))


print(min(my_numbers))
print(max(my_numbers))
print(len(my_numbers))
print(sum(my_numbers))
print(sorted(my_numbers))
