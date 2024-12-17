# Домашнее задание по теме "Декораторы"

# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции
# будет простым числом и "Составное" в противном случае.
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(2, result):
            if result % i == 0:
                print('Составное')
                return result
            else:
                continue
        print('Простое')
        return result

    return wrapper


@is_prime
def sum_three(x, y, z):
    return x + y + z


if __name__ == '__main__':
    # Пример:
    result = sum_three(2, 3, 6)
    print(result)

# Результат консоли:
# Простое
# 11
