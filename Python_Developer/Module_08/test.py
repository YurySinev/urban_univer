try:
    a, b, i = 4, 5, 0
    truba = a + b
    print(truba)
    truba = 10 / i
    print(truba)
except ZeroDivisionError as exc:
    print(f'{exc} На ноль делить нельзя')
except NameError as exc:
    print(f'Непонятно... Что за переменные такие? Вот, что пошло не так: {exc}')

try:
    file = open('blabal.txt')
except IOError as exc:
    print(f'Кое-что пошло не так, а именно: {exc}. Но мы все еще не плаву)))')
finally:
    print('')