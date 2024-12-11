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
set_comp2 = {x: x**2 for x in my_numbers}
print(set_comp2)