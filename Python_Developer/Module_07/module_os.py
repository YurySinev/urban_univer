import module_os
import subprocess

# 1. os.getcwd(): Возвращает текущий рабочий каталог.
# 2. os.listdir(path): Возвращает список файлов и папок в указанном каталоге.
# 3. os.mkdir(path): Создает новую директорию.
# 4. os.makedirs(path): Создает все директории в пути, если они не существуют.
# 5. os.remove(path): Удаляет файл.
# 6. os.rmdir(path): Удаляет пустую директорию.
# 7. os.removedirs(path): Удаляет директорию и все поддиректории, если они пусты.
# 8. os.rename(src, dst): Переименовывает файл или директорию.
# 9. os.path.exists(path): Проверяет существование указанного пути.
# 10. os.path.isfile(path): Проверяет, является ли путь файлом.
# 11. os.path.isdir(path): Проверяет, является ли путь директорией.
# 12. os.path.join(path1, path2): Объединяет пути с учетом особенностей операционной системы.

# print('Текущая директория: ', os.getcwd())
# print(os.listdir('.'))

# if os.path.exists('first'):
#     os.chdir('first')
# else:
#     os.mkdir('first')
#     os.chdir('first')

# os.makedirs(r'second/third')
# os.chdir('..')
# print('Текущая директория: ', os.getcwd())
# os.removedirs('first/second/third')
# os.rmdir('first')
# os.chdir('../..')
print('Текущая директория: ', os.getcwd())
# for i in os.walk('.'):
#     print(i)
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print('Папки: ', dirs)

files = [f for f in os.listdir() if os.path.isfile(f)]
print('Файлы: ', files)
file_path = files[9]
# subprocess.Popen(['open', files[14]]) # это команда для MacOS, открывает текстовый документ
# os.startfile(file_path) # это команда из видео-лекции. Может, под Windows она работает. На MacOS нет.
print(os.stat(files[12])) # информация о файле
print(os.stat(files[7]).st_size)
# os.startfile(files[9])
