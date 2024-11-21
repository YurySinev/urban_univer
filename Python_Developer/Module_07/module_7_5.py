import os
import time
from tabulate import tabulate

directory = "."
table_data = []

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        # print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
        #       f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
        table_data.append([file, filepath, filesize, formatted_time, parent_dir])

headers = ['Обнаружен файл:', 'Путь:', 'Размер:', 'Время изменения:', 'Родительская директория:']
table = tabulate(table_data, headers=headers)
print(table)