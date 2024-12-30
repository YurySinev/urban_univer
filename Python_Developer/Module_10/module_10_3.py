# Домашнее задание по теме "Блокировки и обработка ошибок"
#
# Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.
#
# Задача "Банковские операции":

import threading
import time
import random


class Bank:
    """класс Bank со следующими свойствами:
    balance - баланс банка (int)
    lock - объект класса Lock для блокировки потоков.
    """

    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            try:
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            except Exception:
                pass
            finally:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            if amount <= self.balance:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}')
                time.sleep(0.001)
            else:
                try:
                    print('Запрос отклонён, недостаточно средств')
                    self.lock.acquire()
                    time.sleep(0.001)
                except Exception:
                    pass

    def __repr__(self):
        return f"Итоговый баланс: {self.balance}"


# По итогу вы получите скрипт разблокирующий поток до баланса равному 500 и больше или блокирующий, когда
# происходит попытка снятия при недостаточном балансе.

# Пример результата выполнения программы:
if __name__ == '__main__':
    bk = Bank()
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print()
    print(bk)

# Вывод на консоль (может отличаться значениями, логика должна быть та же):
# Пополнение: 241. Баланс: 241
# Запрос на 174
# Снятие: 174. Баланс: 67
# Пополнение: 226. Баланс: 293
# Запрос на 421
# Запрос отклонён, недостаточно средств
# Пополнение: 133. Баланс: 426
# Запрос на 422
# Снятие: 422. Баланс: 4
# Пополнение: 150. Баланс: 154
# Запрос на 207
# Запрос отклонён, недостаточно средств
# ....
# Запрос на 431
# Снятие: 431. Баланс: 276
# Запрос на 288
# Запрос отклонён, недостаточно средств
# Итоговый баланс: 276
