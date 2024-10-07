# Максимум в списке
# Подсчёт четных чисел в списке
# Уникальный список

my_list = [1, 2, 1, 5, 23, 45, 777, 984, 2634, 0, 2, 2, 3, 4, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 6, 7, 9, 4, 5, 6,
           3, 4, 2, 5, 6, 10, 45, 11, 23, 12, 3, 4, 5, 6, 7, 8]


def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_


print(find_max(my_list))


def count_even(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter


print(count_even(my_list))


def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list


my_list1 = unique(my_list)
print(my_list1)
print(sorted(my_list))

# funcpract1.py
# funcpract1.py. На экране
