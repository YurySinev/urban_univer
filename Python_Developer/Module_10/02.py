import threading
import time
import datetime

class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay
    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'{name} {time.ctime(time.time())}')
            counter -= 1
    def run(self) -> None:
        print(f'Поток {self.name} запущен')
        self.timer(self.name, self.counter, self.delay)
        print(f'Поток {self.name} завершен')

thread1 = MyThread('thread1', 5, 1)
thread2 = MyThread('thread2', 3, 2)
thread1.start()
thread2.start()

# print(time.ctime(time.time()))
# print(datetime.datetime.now())