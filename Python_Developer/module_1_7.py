# Дополнительное практическое задание по модулю: "Базовые структуры данных."

# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#
# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.
#
# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_abc = list(students)  # создаем список из множества
students_abc.sort()  # сортируем его (по умолч. по алфавиту)

# вариант 1 без циклов:
av_grades1 = list(map(lambda x: sum(x) / len(x), grades)) # создаем список со средними оценками
dic_1 = dict(zip(students_abc, av_grades1)) # объединяем два списка в словарь
print(dic_1)

# вариант 2 без циклов:
av_grades2 = (sum(x) / len(x) for x in grades) # создаем список со средними оценками
dic_2 = dict(zip(students_abc, av_grades2)) # объединяем два списка в словарь
print(dic_2)

# вариант 3 с циклом:
average_grades = {} # создаем пустой словарь

for i in range(len(students_abc)):
    # пополняем словарь с одновременным вычислением средней оценки
    average_grades[students_abc[i]] = sum(grades[i]) / len(grades[i])

print(average_grades)
