# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"

# Задача "План перехват":
# Напишите 2 функции:
def personal_sum(*numbers):
    incorrect_data = 0
    number_count = 0
    result = 0
    for i in numbers:
        try:
            if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
                nested_sum, nested_correct, nested_incorrect = personal_sum(*i)
                result += nested_sum
                number_count += nested_correct
                incorrect_data += nested_incorrect
            else:
                result += i
                number_count += 1
        except TypeError as err:
            incorrect_data += 1

    return result, number_count, incorrect_data


def calculate_average(*numbers):
    sum, number_count, incorrect_data = personal_sum(numbers)
    average = 0
    try:
        average = sum / number_count
    except ZeroDivisionError:
        return 0
    # except TypeError:
    #     return f'Некорректный тип данных для подсчёта суммы - {}'
    # for i in numbers:
    #     try:
    #         i / 2
    #     except TypeError as err:
    #         print(f'Некорректный тип данных для подсчёта суммы - {i}')

    # return sum
# Среднее арифметическое - сумма всех данных делённая на их количество.
# 1. Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
# 2. Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
# 3. Т.к. коллекция numbers может оказаться пустой,
# то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
# 4. Также в numbers может быть записана не коллекция, а другие типы данных, например числа.
# Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'.
# В таком случае функция просто вернёт None.

# Пункты задачи:
# Создайте функцию personal_sum на основе условий задачи.
# Создайте функцию calculate_average на основе условий задачи.
# Вызовите функцию calculate_average несколько раз, передав в неё данные разных вариаций.

# Пример выполнения программы:

if __name__ == '__main__':
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать

# Вывод на консоль:
# Некорректный тип данных для подсчёта суммы - 1
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 2
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 3
# Результат 1: 0
# Некорректный тип данных для подсчёта суммы - Строка
# Некорректный тип данных для подсчёта суммы - Ещё Строка
# Результат 2: 2.0
# В numbers записан некорректный тип данных
# Результат 3: None
# Результат 4: 26.5
