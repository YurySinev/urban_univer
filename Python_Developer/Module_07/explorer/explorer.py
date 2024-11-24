#
# Этот скрипт должен корректно работать на MacOS, Windows и Linux
#
import tkinter
import os
import subprocess  # это для Мака и Линукса
from tkinter import filedialog
import platform  # проверка - какая операционка?


# выбираем команду открытия файла в зависимости от операционки:
def open_file(filename):
    if platform.system() == 'Windows':
        os.startfile(filename)
    elif platform.system() == 'Darwin':  # macOS
        subprocess.call(['open', filename], shell=False)
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', filename], shell=False)


# выбор файла:
def file_select():
    filename = filedialog.askopenfilename(initialdir='.', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = 'Файл: ' + filename
    # os.startfile(filename)
    open_file(filename)


window = tkinter.Tk()
# параметры окна:
window.title('Проводник')
window.geometry('650x150')
window.configure(bg='black')
window.resizable(False, False)

# текстовое поле:
text = tkinter.Label(window, text='Файл: ', height=5, width=75, background='silver', foreground='blue')
text.grid(column=1, row=1)

# кнопка выбора:
button_select = tkinter.Button(window, text='Выбрать файл', width=20, height=3,
                               background='silver', foreground='blue', command=file_select)
button_select.grid(column=1, row=2, pady=1)

window.mainloop()
