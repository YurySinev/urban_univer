import threading
from threading import Thread, Event
import time

def first_worker():
    print('Первый рабочий начал работу')
    event.wait()
    print('Первый рабочий продолжил работу')
    time.sleep(4)
    print('Первый рабочий закончил работу')

def second_worker():
    print('Второй рабочий начал работу')
    print('Второй рабочий продолжил работу')
    time.sleep(5)
    print('Второй рабочий закончил работу')
    print('Event...')
    event.set()


event = Event()
print(event.is_set())

thread1 = threading.Thread(target=first_worker)
thread2 = threading.Thread(target=second_worker)
thread1.start()
thread2.start()

