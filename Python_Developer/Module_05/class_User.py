import hashlib


class User:
    """
    Класс User: nickname, password, age. А также хэширование пароля и проверка на длину и символы (по желанию)
    """

    # простой пароль без повторения (для данной задачи):
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # (имя пользователя, строка)
        self.password = self.hash_password(password)
        self.age = age  # (возраст, число)

    # сложный пароль c проверкой и с повторным введением пароля:
    # def __init__(self, nickname, password, password_confirm, age):
    #     self.nickname = nickname # имя пользователя
    # if len(password) >= 8 and self.check_password(password)\
    #                 and password == password_confirm:
    #     self.password = self._hash_password(password)
    # else:
    #     print(
    #         f"Пароль должен быть не менее 8 символов в длину и содержать \n"
    #         f"как минимум одну заглавную букву, "
    #         f"одну цифру и один специальный символ")
    #     return self.__init__(username, input("Введите пароль: "), input("Введите пароль еще раз: "))

    # проверка сложности пароля:
    def check_password(self, pswd):
        # наборы символов:
        symbols = [chr(i) for i in range(33, 48)]  # спецсимволы
        caps = [chr(i) for i in range(65, 91)]  # ЗАГЛАВНЫЕ БУКВЫ
        nums = [i for i in range(0, 10)]  # цифры
        # letters = [chr(i) for i in range(97, 123)]
        # проверка наличия символов из наборов в пароле:
        if any(c in pswd for c in symbols) and any(c in pswd for c in caps) \
                and any(c in pswd for c in str(nums)):
            return True
        else:
            return False

    @classmethod  # хэширование пароля:
    def hash_password(cls, password):
        _hash = hashlib.sha256(password.encode()).hexdigest()
        hash_int = int(_hash, 16)
        return hash_int


if __name__ == '__main__':
    # проверки
    symbols = [chr(i) for i in range(33, 48)]  # некоторые спецсимволы
    caps = [chr(i) for i in range(65, 91)]  # ЗАГЛАВНЫЕ БУКВЫ
    nums = [i for i in range(0, 10)]  # цифры
    print(symbols)
    print(caps)
    print(nums)

    u1 = User('Yury', 'lolkekcheburek', 63)
    print(u1.password)
    print(u1.check_password('fddi123QW)'))
    u2 = User('Lena', 'asdf1#QW', 66)
    print(u2.password)
    print(u1.password == u2.password)
    mypass = User._hash_password('asdf1#QW')
    print(mypass == u2.password)
    print(mypass)
