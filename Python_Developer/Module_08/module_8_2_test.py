from module_8_2 import personal_sum, calculate_average

# Неверно понял условие задачи, не обратил внимания на слова "коллекцию numbers":
# print(calculate_average(1, 2, [[3, '3'], (4, '5')], 5, '6'))

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
