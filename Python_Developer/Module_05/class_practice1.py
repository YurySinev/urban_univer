class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        # сложный пароль c проверкой:
        if len(password) >= 8 and self.check_password(password) \
                and password_confirm == password_confirm:
            self.password = password
        else:
            print(
                f"Пароль должен быть не менее 8 символов в длину и содержать \nкак минимум одну заглавную букву, "
                f"одну цифру и один специальный символ")
            return self.__init__(username, input("Введите пароль: "), input("Введите пароль еще раз: "))

        # простой пароль и простая проверка (для тестирования):
        # if password == password_confirm:
        #     self.password = password
        # else:
        #     print("Пароли не совпадают. Повторите ввод.")
        #     return self.__init__(username, input("Введите пароль: "), input("Введите пароль еще раз: "))
        self.email = None

    def __str__(self):
        return f"Пользователь: {self.username}, пароль: ****"

    # проверка сложного пароля:
    def check_password(self, pswd):
        # наборы символов:
        symbols = [chr(i) for i in range(33, 48)]
        caps = [chr(i) for i in range(65, 91)]
        nums = [i for i in range(0, 10)]
        letters = [chr(i) for i in range(97, 123)]
        # проверка наличия символов из наборов в пароле:
        if any(c in pswd for c in symbols) and any(c in pswd for c in caps) \
                and any(c in pswd for c in str(nums)):
            return True
        else:
            return False


class Database():
    """
    База данных. Словарь: пользователи, пароли
    """

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствуем Вас! Выберите действие: \n"
                           "1. Вход \n2. Регистрация"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Вход выполнен, {login}")
                    break
                else:
                    print("Пароль неверный")
            else:
                print("Пользователь не найден")
        if choice == 2:
            user = User(input("Введите логин: "), pass1 := input("Введите пароль: "),
                        pass2 := input("Введите пароль еще раз: "))
            if pass1 != pass2:
                continue
                # exit()
            database.add_user(user.username, user.password)
            print(database.data)
