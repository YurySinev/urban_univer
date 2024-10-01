def divine(x, y):
    if y == 0:
        return "Ой-ой-ой! Ошибка! На ноль делить низя!"
    else:
        return x / y


if __name__ == "__main__":
    print(divine(27, 45))
    print(divine(555, 0))
    print(divine(114, 7))
