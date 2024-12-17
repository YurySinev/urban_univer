# Домашнее задание по теме "Генераторы"

# Задача:
# Напишите функцию-генератор all_variants(text), которая принимает строку text
# и возвращает объект-генератор, при каждой итерации которого будет возвращаться
# подпоследовательности переданной строки.

# Пункты задачи:
# Напишите функцию-генератор all_variants(text).

def all_variants(text):
    for i in range(1, len(text) + 1):
        for j in range(len(text) - i + 1):
            yield text[j:j + i]


if __name__ == '__main__':
    # Пример результата выполнения программы:
    a = all_variants("abcdef")
    for i in a:
        print(i)

# Вывод на консоль:
# a
# b
# c
# d
# e
# f
# ab
# bc
# cd
# de
# ef
# abc
# bcd
# cde
# def
# abcd
# bcde
# cdef
# abcde
# bcdef
# abcdef