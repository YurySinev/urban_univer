# пример 1 - создание простого генератора:

def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1


obj = func_generator(50)
print(obj)
for i in obj:
    print(i, end=' ')

print()
# пример 2 - снова Фибоначчи:
print()


def fibonacci_v2(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


fib = fibonacci_v2(30)
# print(fib)
for i in fib:
    print(i, end=' ')


# ВНИМАНИЕ! Генреаторные выражения, генераторную сборку и все,
# что связано с генераторами можно прочитать ТОЛЬКО ОДИН РАЗ!
# Второй раз вот это уже не читается:
# for i in fib:
#     print(i, end=' ')

print()
# пример 3 - можно сделать бесконечный список значений:
print()
def fibonacci_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# for value in fibonacci_v3():
#     print(value, end=' ')
#     # Даже с такими дикими значениями вычисления происходят очень быстро:
#     if value > 10 ** 666:
#         break

print()
# пример 4 - замер времени выполнения:
print()

import time

start = time.time()

def read_large_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

for line in read_large_file('hw_mod_9_6.txt'):
    print(line)

fin = time.time()

print((fin - start) * 1000)

