import threading
import time


# print(threading.enumerate()) # список всех активных потоков
# print(threading.current_thread()) # какой поток выполняется?

def func1():
    for i in range(10):
        time.sleep(0.5)
        print(i, threading.current_thread())
        # print(threading.current_thread().is_alive())


def func2(x):
    for i in range(x):
        time.sleep(1)
        print(i, threading.current_thread())
        # print(threading.current_thread().is_alive())

# объект потока. Аргументы: target - запускаемая функция, args - параметры, которые надо передать внутрь
thread = threading.Thread(target=func2, name='Поток 2', args=(10,), daemon=True)
thread.start() # запуск потока
# thread.join()
print(thread.is_alive())
func1()
print(threading.enumerate())
print(threading.current_thread())

