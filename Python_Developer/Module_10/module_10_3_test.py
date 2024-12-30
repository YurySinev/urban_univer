import random
import threading
from module_10_3 import Bank

# print(random.randint(50, 500))
bk = Bank()
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)
th1.start()
th2.start()
th1.join()
th2.join()

print(bk)