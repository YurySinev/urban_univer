# Домашнее задание по теме "Создание исключений"
# Задача "Некорректность":

class IncorrectVinNumber(Exception):
    def __init__(self, message=""):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message=""):
        self.message = message


class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model  # название автомобиля (строка)
        if self.__is_valid_vin(vin):
            self.__vin = vin  # vin номер автомобиля (целое число), private
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers  # номер авто (строка), private

    def __is_valid_vin(self, vin_number) -> bool:  # проверка vin  номера, private
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers: str) -> bool:  # проверка номера авто, private
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


# Пример результата выполнения программы:
# Пример выполняемого кода:
if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

# Вывод на консоль:
# Model1 успешно создан
# Неверный диапазон для vin номера
# Неверная длина номера
