# from multiprocessing import Pool
#
# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))

from multiprocessing import Pool
import time


# Функция, которую будем выполнять параллельно
def square_number(x):
    time.sleep(1)  # Имитация долгой операции
    return x * x


if __name__ == '__main__':
    # Создаем пул процессов с 3 рабочими процессами
    with Pool(processes=3) as pool:
        # Задаем список чисел для обработки
        numbers = (n for n in range(1, 20))
        # print(numbers)
        # Применяем функцию square_number к каждому элементу списка параллельно
        results = pool.map(square_number, numbers)

    # Выводим результаты
    print(results)
