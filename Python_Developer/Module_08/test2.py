# Сложные моменты и исключения в стеке вызовов функции

def f1(number):
    return total / number


def f2():
    # print('Какой хороший день')
    # result_f1 = f1(0)
    # return result_f1

    # summ = 0
    # for i in range(-5, 5):
    #     if i == 0: continue
    #     else:
    #         print(summ)
    #         summ += f1(i)
    # return summ

    summ = 0
    for i in range(-2, 2):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'Внутри f1 что-то пошло не так: {exc}. Но программа жива. Мы молодцы.')
    return summ / 1



try:
    total = f2()
    print(total)
except NameError as exc:
    print(f'Вот, что пошло не так - {exc}, но мы устояли')
