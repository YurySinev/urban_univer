# Задание 1
# 1. Написать функцию, которая возвращает функцию повторения первых двух символов «n» раз.
# 2. Создать массив функций и применить все функции поочерёдно к аргументу.
# 3. Применить все функции поочерёдно к массиву аргументов.

# 1
def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + '-') * n + animal

    return repeat


animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик', 'кися', 'Пуся']

test1 = gen_repeat(1)
test2 = gen_repeat(2)

print(test1(animal))
print(test2(animal))

# 2
repetitions = [gen_repeat(n) for n in range(3)]
# for i in repetitions:

result = [func(animal) for func in repetitions]
print(result)

# 3
fin_result = [func(x) for func in repetitions for x in animals]
print(fin_result)
fin_result2 = [func(x) for x in animals for func in repetitions]
print(fin_result2)

print()
# Задача: есть функция, которая возвращает результат возведения числа a в степень b.
# Нужно ускорить ее, чтобы она не делал повторные вычисления.

def memorize_func(f):
    mem = {} # сюда сохраняются аргументы и результаты, и при повторном вызове функции с теми же
    # аргументами, функция не выполняется, а берется уже сохраненный результат

    def wrapper(*args):
        print(f'Выполнение функции с аргументами = {args}, внутренняя память = {mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась, ответ = {mem[args]}'
        else:
            return f'Функция уже была выполнена ранее, ответ = {mem[args]}'

    return wrapper

@memorize_func
def func(a, b):
    print(f'Возводим {a} в степень {b}')
    return a ** b


print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')
