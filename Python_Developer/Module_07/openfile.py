from pprint import pprint

# name = 'sample.txt'         # 0. Переменная с именем;
# file = open(name, 'r')      # 1. Открытие файла;
# print(file.read())         # 2. Выполнение действия;
# file.close()                # 3. Закрытие файла.

# Разница между print и pprint:
# Вывод print(file.read()) - чистый текст:
    # Это специальный текст для теста
    # Вторая строка текста
    # Третья строка текста
    # Четвертая строка текста
# Вывод pprint(file.read()):
    # ('Это специальный текст для теста\n'
    #  'Вторая строка текста\n'
    #  'Третья строка текста\n'
    #  'Четвертая строка текста')

# name = 'sample.txt'
# file = open(name, 'r')
# pprint(file.read())
# file.close()

name = 'sample2.txt'
file2 = open(name, 'a+')
print(file2.tell()) # положение курсора
file2.write('\nСевильский цирюльник')
file2.seek(11)
pprint(file2.read()) # читает, но курсор уже в конце файла
file2.close()

