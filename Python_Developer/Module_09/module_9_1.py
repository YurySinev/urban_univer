# Домашнее задание по теме "Введение в функциональное программирование"
# Задача "Вызов разом"

def apply_all_func(int_list: list, *functions: tuple) -> dict:
    """
    Принимает список чисел int_list и неопределенное число функций, применимых к этим спискам.
    Вызывает каждую функцию к переданному списку int_list и возвращает словарь, где ключ -
    название вызванной функции, а значение - её результат работы со списком int_list.
    """
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result


# Пример работы кода:
if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# Вывод на консоль:
# {'max': 20, 'min': 6}
# {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
