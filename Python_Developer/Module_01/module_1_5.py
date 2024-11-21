# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

# Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = 3, 5, 7, 34, 3.14, 'Петя', 'волк'

# Выполните операции вывода кортежа immutable_var на экран.
print(immutable_var)

# Попытайтесь изменить элементы кортежа immutable_var.
# immutable_var[0] = 2
# TypeError: 'tuple' object does not support item assignment

# Объясните, почему нельзя изменить значения элементов кортежа.
# Кортеж - неизменяемый тип данных.

# Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list = [3, 5, 7, 34, 3.14, 'Петя', 'волк']

# Измените элементы списка mutable_list.
mutable_list[0] = 2
mutable_list.extend('дом')
mutable_list.append(['машина', "гараж"])
mutable_list.remove(34)

# Выведите на экран измененный список mutable_list.
print(mutable_list)
