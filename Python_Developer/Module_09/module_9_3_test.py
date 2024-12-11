first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

result = {i: len(first[i]) == len(second[i]) for i in range(min(len(first), len(second)))}

print(result)