class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password
        else:
            print("Пароли не совпадают. Повторите ввод.")
            return self.__init__(username, input("Введите пароль: "), input("Введите пароль еще раз: "))
        self.email = None

    def __str__(self):
        return f"Пользователь: {self.username}, пароль: ****"


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
    user = User(input("Введите логин: "), input("Введите пароль: "), input("Введите пароль еще раз: "))
    print(user)
    database.add_user(user.username,user.password)
    print(database.data)
