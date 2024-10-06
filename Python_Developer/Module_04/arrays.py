# import random
import time
from sortfunc import bubble_sort, bubble_sort2, selection_sort, insertion_sort

nums1 = [37, 46, 12, 37, 7, 36, 13, 21, 19, 48, 15, 9, 21, 16, 50, 34, 17, 15, 32, 18, 22, 16, 44, 14, 16, 23, 8, 37,
         28, 43, 11, 6, 28, 7, 41, 24, 45, 6, 10, 15, 15, 49, 19, 17, 5, 39, 23, 32, 40, 30]
nums2 = [60, 26, 10, 33, 2, 47, 16, 45, 34, 3, 24, 14, 50, 32, 35, 37, 20, 67, 24, 40, 36, 24, 81, 25, 83, 45, 84, 29,
         16, 50, 83, 51, 14, 56, 20, 13, 77, 31, 44]
nums3 = [43, 17, 100, 47, 31, 55, 59, 95, 97, 86, 45, 4, 48, 31, 36, 95, 71, 2, 95, 60, 55, 78, 83, 15, 87, 73, 97, 39,
         89, 91, 62, 11, 46, 54, 54, 73, 4, 84, 96, 94, 42, 2, 28, 87, 95, 10, 29]


# nums = [random.randint(1, 85) for i in range(39)]
# print(nums)

# Декоратор для замера времени выполнения функции
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Записываем время начала выполнения функции
        result = func(*args, **kwargs)  # Выполняем функцию
        end_time = time.time()  # Записываем время окончания выполнения функции
        execution_time = end_time - start_time  # Вычисляем время выполнения
        print(f"Функция {func.__name__} выполнилась за {execution_time} секунд")
        return result

    return wrapper

ct = calculate_time
nums = [nums1, nums2, nums3]
sort_funcs = [ct(bubble_sort), ct(bubble_sort2), ct(selection_sort), ct(insertion_sort)]

for func in sort_funcs:
    for j in nums:
        result = print(func(j))
