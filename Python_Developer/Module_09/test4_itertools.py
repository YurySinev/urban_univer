# пример 1 - библиотека itertools

import sys
from itertools import repeat

ex_iterator = repeat("4", 100000)
print(ex_iterator)
print(f"Размер итератора: {sys.getsizeof(ex_iterator)}")


# ex_str = "4" * 100000
# # print(ex_str)
# print(f"Размер строки: {sys.getsizeof(ex_str)}")
# print(sys.getsizeof(ex_str) / sys.getsizeof(ex_iterator))

# пример 2 - класс-итератор

class Iter:
    def __init__(self):
        self.first = "Первый элемент"
        self.second = "Второй элемент"
        self.third = "Третий элемент"
        self.forth = "Четвертый элемент"
        self.fifth = "Пятый элемент"
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i == 1:
            return self.first
        if self.i == 2:
            return self.second
        if self.i == 3:
            return self.third
        if self.i == 4:
            return self.forth
        if self.i == 5:
            return self.fifth
        if self.i == 6:
            print("Подсчет закончен")
        raise StopIteration


obj = Iter()
# print(obj)

# try:
#     for v in obj:
#         print(v)
# except StopIteration:
#     print("Stop!")

try:
    while True:
        value = obj.__next__()
        print(value)
except StopIteration:
    pass


# пример 3 - числа Фибоначчи: функция vs. итератор:

def fibonacci(n):
    i = 0
    a, b, = 0, 1
    while i < n:
        print(a, end=' ')
        a, b = b, a + b
        i += 1


fibonacci(30)

print()


def fibonacci_2(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


print(fibonacci_2(30))


# а теперь - на основе итератора:

class Fibonacci:
    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b

        return self.a

fib = Fibonacci(30)

try:
    for i in fib:
        print(i, end=' ')
except StopIteration:
    pass