# Домашнее задание по теме "Форматирование строк".
# Пример входных данных
team1 = "Мастера кода"
team2 = "Волшебники данных"
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print()
# Использование %:
# Переменные: количество участников первой команды (team1_num).
print("В команде %s участников: %d ! " % (team1, team1_num))
print("В команде %s участников: %d ! " % (team2, team2_num))

# Переменные: количество участников в обеих командах (team1_num, team2_num).
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
print()
# Использование f-строк:
# Переменные: количество решённых задач по командам: score_1, score_2
print(f'Команды решили {score_1} и {score_2} задач. В среднем по {time_avg} секунд на задачу.')

# Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
print("\tКоманда {} решила задач: {} !".format(team1, score_1))
print(f'Среднее время решения одной задачи у команды {team1}: {team1_time / score_1:.1f} секунд.')
print("\tКоманда {team} решила задач: {score} !".format(score=score_2, team=team2))
print(f'Среднее время решения одной задачи у команды {team2}: {team2_time / score_2:.1f} секунд.')

# Переменные: время за которое команда 2 решила задачи (team1_time).
print("\tМастера кода решили задачи за {} с !".format(team1_time))

print("\tВолшебники данных решили задачи за {0} с !".format(team2_time))
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f'Победа команды {team1}!')
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Победа команды {team2}!')
else:
    print('Ничья!')







# Переменные: исход соревнования (challenge_result).
# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
