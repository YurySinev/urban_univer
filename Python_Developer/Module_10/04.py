# очереди в потоках

from queue import Queue
import time
import threading


def getter(queue):
    while True:
        time.sleep(5)
        item = queue.get()
        print(threading.current_thread(), 'взял элемент', item)


q = Queue(maxsize=10)
thread1 = threading.Thread(target=getter, args=(q,), daemon=True)
thread1.start()

for i in range(10):
    time.sleep(2)
    q.put(i)
    print(threading.current_thread(), 'положил в очередь', i)

# q.put(5)
# print(q.get(timeout=2))
print('Конец программы')
