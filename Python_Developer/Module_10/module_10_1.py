# Домашнее задание по теме "Введение в потоки".
# Задача "Потоковая запись в файлы"

import threading
import datetime
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово №{i + 1}\n")
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


# Выполнение задачи без использования потоков:
start_time = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(f'Работа потоков {elapsed_time}')  # 0:00:35.230676

# Аналогичная задача, но с применением потоков:
start_time = datetime.datetime.now()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(f'Работа потоков {elapsed_time}')  # 0:00:20.741808
