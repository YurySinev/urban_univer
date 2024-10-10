class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password
        self.email = None

    def __str__(self):
        return f"Пользователь: {self.username}, пароль: ****"


class Database():
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


if __name__ == '__main__':
    database = Database()
    user = User(input("Введите логин: "), input("Введите пароль: "), input("Введите пароль еще раз: "))
    print(user)
