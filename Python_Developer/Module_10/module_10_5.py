# Домашнее задание по теме "Многопроцессное программирование"
# Задача "Многопроцессное считывание":
# Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.

import time
from multiprocessing import Pool


def read_info(name):
    all_data = []  # создаем локальный список
    with open(name, 'r') as file:
        line = file.readline().strip()  # читаем первую строку и обрезаем символ переноса строки
        while line:  # если строка не пустая, то
            all_data.append(line)  # добавляем ее в список и
            line = file.readline().strip()  # считываем следующую строку


if __name__ == '__main__':
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

    start_time = time.time()

    # Линейный вызов:
    # for f in filenames:
    #     read_info(f)

    # Многопроцессный вызов:
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    stop_time = time.time()
    elapsed_time = stop_time - start_time
    print(elapsed_time)
    # 7.686239004135132 (линейный)
    # 3.879276990890503 (многопроцессный)
