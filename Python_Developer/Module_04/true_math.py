from math import inf


def divine(x, y):
    if y == 0:
        return f"{x} / {y} = {inf}"
    else:
        return x / y

if __name__ == '__main__':
    print(divine(57, 3))
    print(divine(63, 0))
    print(divine(263548, 8739))


