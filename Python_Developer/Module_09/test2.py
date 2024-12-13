##########################################################
# пример 1 - как выглядит объединение функций map и filter:

def by_3(x):
    return x * 3


def is_odd(x):
    return x % 2


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = map(by_3, filter(is_odd, my_numbers))
print(list(result))

#############################
# пример 2 - списковая сборка:
# аналог map
#############################

list_comp_1 = [x * 3 for x in my_numbers]
print(list_comp_1)

##################################
# пример 3 - списковая сборка с if:
# аналог filter
##################################

list_comp_2 = [x * 3 for x in my_numbers if x % 2]
print(list_comp_2)

###################################
# пример 4 - условие перед циклом:
# (для того, чтобы не отфильтровать данные, а поменять операции над ними)

list_comp_3 = [x * 2 if x > 2 else x * 10 for x in my_numbers]
print(list_comp_3)

my_numbers2 = ['A', 1, 4, 'B', 5, 'C', 2, 6]
list_comp_4 = [x if type(x) == str else x * 5 for x in my_numbers2]
print(list_comp_4)

##########################################
# пример 5 - можно делать вложенные списки:
##########################################
# my_numbers
they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]

list_comp_5 = [x * y for x in my_numbers for y in they_numbers]
print(list_comp_5)

list_comp_6 = [x * y for x in my_numbers for y in they_numbers if x % 2]
print(list_comp_6)

list_comp_7 = [x * y for x in my_numbers for y in they_numbers if x % 2 and y // 2]
print(list_comp_7)

########################################################
# пример 6 - можно создавать на лету множества и словари:
########################################################

# my_numbers
set_comp = {x for x in my_numbers}
print(set_comp)

# they_numbers
set_comp2 = {x: x ** 2 for x in my_numbers}
print(set_comp2)

###############################
# пример 7 - ленивые вычисления:
###############################

generator = (x ** 1000 for x in my_numbers)
print(generator)

#################################################################
# пример 8 - прочитать генераторную сборку можно только один раз:
#################################################################

for elem in generator:
    print(elem)
print("Еще разок...")
for elem in generator:
    print(elem)
print("Облом!")

#############################################################################################
# пример 9 - генераторные сборки используются там, где надо производить затратные вычисления:
#############################################################################################

import time

start_time = time.time()

# my_numbers - те же
# result = [x**3000 for x in my_numbers]
result = (x ** 3000 for x in my_numbers)
print(result)

for i in result:
    print(i)

finish_time = time.time()
print(f"Время в миллисекундах: {(finish_time - start_time) * 1000}")

# Время в миллисекундах: 1.302957534790039 - генератор списка
# Время в миллисекундах: 0.7040500640869141 - генераторная сборка
###################################################################
# пример 10 - демонстрация встроенных функций с ленивым вычислением:
###################################################################

list_1 = [1, 5, 9, 29, 4, 15, 77, 93]
list_2 = [5, 2, 9, 1, 2, 7, 9, 8]

ran = range(10, 30)
zp = zip(list_1, list_2)
mp = map(str, list_1)

print(ran, zp, mp)

print(list(ran))
print(list(zp))
print(list(mp))
