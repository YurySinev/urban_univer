# Домашнее задание по теме "Позиционирование в файле".

# Задача "Записать и запомнить"

def custom_write(file_name: str, strings: list):
    # Записывает в файл file_name все строки из списка strings, каждая на новой строке.
    # Возвращает словарь strings_positions, где ключом будет кортеж
    # (<номер строки>, <байт начала строки>), а значением - записываемая строка.
    # Для получения номера байта начала строки используйте метод tell() перед записью.
    string_positions = {}
    count = 0
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        position = file.tell()
        file.write(i + '\n')
        string_positions[(strings.index(i) + 1, position + count)] = i
        count += 1
    file.close()
    return string_positions


# Пример результата выполнения программы:
# Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')

# Как выглядит файл после запуска:
# Text for tell.
# Используйте кодировку utf - 8.
# Because there are 2 languages!
# Спасибо!

