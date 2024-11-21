# повторяю за видеозаписью:
def check_winner():
    if turn > 4:  # проверка раньше пятого хода бессмысленна
        for w in ["X", "0"]:  # чтобы не дублировать всю эту писанину
            if area[0][0] == w and area[0][1] == w and area[0][2] == w:
                return w
            if area[1][0] == w and area[1][1] == w and area[1][2] == w:
                return w
            if area[2][0] == w and area[2][1] == w and area[2][2] == w:
                return w
            if area[0][0] == w and area[1][0] == w and area[2][0] == w:
                return w
            if area[1][0] == w and area[1][1] == w and area[1][2] == w:
                return w
            if area[2][0] == w and area[2][1] == w and area[2][2] == w:
                return w
            if area[0][0] == w and area[1][1] == w and area[2][2] == w:
                return w
            if area[2][0] == w and area[1][1] == w and area[2][0] == w:
                return w
        return "*"
    else:
        return "*"

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

def draw_area():
    for i in area:
        print(*i)  # * - оператор распаковки
    print()


print("Добро пожаловать в крестики-нолики")
print("----------------------------------")
draw_area()
for turn in range(1, 10):
    print(f"Ход: {turn}")
    if turn % 2 == 0:
        turn_char = '0'
        print("Ходят нолики")
    else:
        turn_char = 'X'
        print("Ходят крестики")
    row = int(input("Введите номер строки (1,2,3) ")) - 1  # -1 = юзер френдли
    column = int(input("Введите номер столбца (1,2,3) ")) - 1
    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print("Ячейка уже занята. Вы пропускаете ход.")
        draw_area()
        continue

    draw_area()

    if check_winner() == "X":
        draw_area()
        print("Победа крестиков")
        break
    if check_winner() == "0":
        draw_area()
        print("Победа ноликов")
        break
    if check_winner() == "*" and turn == 9:
        print("Ничья")
