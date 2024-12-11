# Домашнее задание по теме "Списковые, словарные сборки"
#
# Цель: закрепить знания о списочных и словарных сборках, решив несколько небольших задач.
#
# Задача:
# Даны несколько списков, состоящих из строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список, состоящий из длин строк списка first_strings, при условии,
# что длина строк не менее 5 символов:
first_result = [len(x) for x in first_strings if len(x) > 4]

# Список, состоящий из пар слов (кортежей) одинаковой длины. Каждое слово
# из списка first_strings должно сравниваться с каждым из second_strings:
second_result = [(x, y) for x in first_strings for y in second_strings if len(x)==len(y)]

# Словарь, где пара ключ-значение - строка : длина строки. Значения строк -
# из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки.
third_result = {x: len(x) for x in first_strings}
third_result.update({y: len(y) for y in second_strings})

# Пример результата выполнения программы:
# Пример выполнения кода:
if __name__ == '__main__':
    print(first_result)
    print(second_result)
    print(third_result)

# Вывод на консоль:
# [10, 8, 8]
# [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
