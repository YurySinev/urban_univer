from dis import dis
def divine(x=15, y=5):
    if y == 0:
        return "Ой-ой-ой! Ошибка! На ноль делить низя!"
    else:
        return x / y


if __name__ == "__main__":
    print(divine(27, 45))
    print(divine(555, 0))
    print(divine(15, 3))
    dis(divine)
