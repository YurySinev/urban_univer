import tkinter
import subprocess
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir='.', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = 'Файл: ' + filename
    subprocess.call(['open', filename], shell=True)


window = tkinter.Tk()
window.title('Проводник')
window.geometry('650x150')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл: ', height=5, width=70,
                     background='silver', foreground='blue')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, text='Выбрать файл', width=20, height=3, background='silver',
                               foreground='blue', command=file_select)
button_select.grid(column=1, row=2, pady=1)
window.mainloop()
