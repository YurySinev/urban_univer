# практика по модулю 8. Работа с исключениями

def calc(line: str):
    """
    Принимает строку из файла, разбивает ее на два операнда и математический оператор между ними.
    Вычисляет и возвращает результат
    """
    operand1, operation, operand2 = line.split(' ')
    operand1, operand2 = int(operand1), int(operand2)
    if operation=="+":
        return operand1 + operand2
    elif operation=="-":
        return operand1 - operand2
    elif operation == "*":
        return operand1 * operand2
    elif operation=="/":
        return operand1 / operand2
    elif operation=="//":
        return operand1 // operand2
    elif operation=="%":
        return operand1 % operand2
    # print(operand1, operation, operand2)

line_count = 0

with open('calc.txt', 'r') as file:
    for line in file:
        line_count += 1
        try:
            # print(f"Результат: {calc(line)}")
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Ошибка в строке {line_count}. Не хватает данных для ответа')
            else:
                print(f'Ошибка в строке {line_count}. Нельзя перевести в число')
