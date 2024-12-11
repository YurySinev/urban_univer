first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print(list(result))
print(list(result))

# Консоль:
# [False, False, True]
# [] - "ленивые" вычисления