# Проблемы многопоточного программирования, блокировки и обработка ошибок

import threading

lock = threading.Lock() # 1. Создаем замок
counter = 0

print('Замок есть' if lock.locked() else 'Замка НЕТ')

"""def increment(name):
    global counter
    # ПЕРВЫЙ способ поставить замок: 
    lock.acquire() # 2. Ставим замок
    for i in range(50):
        counter += 1
        print(name, counter)
    lock.release() # 3. Снимаем замок"""

def increment(name):
    global counter
    # ВТОРОЙ способ поставить замок:
    with lock:
        for i in range(50):
            counter += 1
            print(name, counter, 'На замке' if lock.locked() else 'Открыто')

def decrement(name):
    global counter
    # ТРЕТИЙ способ поставить замок:
    try:
        lock.acquire()
        for i in range(50):
            counter -= 1
            print(name, counter, 'Заперто' if lock.locked() else 'Нараспашку')
    except Exception:
        pass
    finally:
        lock.release()


thread1 = threading.Thread(target=increment, args=('Увеличение',))
thread2 = threading.Thread(target=decrement, args=('Уменьшение',))
thread1.start()
thread2.start()
