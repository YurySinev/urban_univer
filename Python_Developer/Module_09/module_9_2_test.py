from module_9_2 import *

# Пример результата выполнения программы:
# Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)

# Вывод на консоль:
# [10, 8, 8]
# [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}

first_strings = ['apple', 'banana', 'cherry']
second_strings = ['orange', 'pear', 'grape']

result = {x: len(x) for x in zip(first_strings, second_strings)}
print(result)