# Дополнительное практическое задание по модулю: "Классы и объекты."
#
# Задание "Свой YouTube"

import time
from class_User import User
from class_Video import Video


class UrTube:
    """
    Класс для взаимодействия с платформой. Cодержит методы добавления видео,
    авторизации и регистрации пользователя и т.д.
    """
    users = {}  # список объектов User
    videos = []  # список объектов Video
    current_user = ''  # текущий пользователь, User
    current_second = 0

    def register(self, nickname, password, age):
        # добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        # После регистрации, вход выполняется автоматически.
        if nickname not in self.users:
            self.users[nickname] = User.hash_password(password), age  # юзера,пароль,возраст > в словарь
            user = User(nickname, password, age)  # создаем объект User
            self.current_user = nickname # автоматический вход
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_in(self, nickname, password):
        # пытается найти пользователя в users с такими же логином и паролем.
        # Если такой пользователь существует, то current_user меняется на найденного.
        # Пароль сравнивается по хэшу.
        if nickname in self.users and User.hash_password(password) == self.users[nickname]:
            self.current_user = nickname
            return f'Вход выполнен'
        else:
            return f'Пользователь не найден'

    def log_out(self, nickname):
        # Сброс текущего пользователя на None.
        if ur.current_user == nickname:
            ur.current_user = None
            print(ur.current_user)

    def add(self, *args):
        # Добавляет объекты класса Video в videos.
        for item in args:
            if item in UrTube.videos:
                continue
            else:
                UrTube.videos.append(item)

    def get_videos(self, word) -> list:
        # Возвращает список названий всех видео, содержащих поисковое слово:
        search_results = []
        for item in UrTube.videos:
            if word.lower() in item.title.lower():
                search_results.append(item.title)
        return search_results

    def watch_video(self, video):
        # Принимает название фильма, если находит - ведётся отсчёт в консоль
        # на какой секунде ведётся просмотр.
        #
        have_video = False
        for i in self.videos: # проверяем, есть ли такой фильм
            if video == i.title:
                have_video = True  # да, имеется
                video = i  # вместо названия подставляем сам объект
                break
        if have_video: # поскольку фильм имеется, то
            if self.current_user:  # если это текущий пользователь
                # проверяем возрастные ограничения
                if self.users[self.current_user][1] < 18 and video.adult_mode is True:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                else:  # ограничений нет, воспроизведение видео
                    video.time_now = self.current_second
                    for i in range(video.time_now + 1, video.duration + 1):
                        print(i, end=' ')
                        time.sleep(1)
                        self.current_second += 1 # счетчик секунд проигрывания видео
                    print("Конец видео")
                    self.current_second = 0 # обнуление счетчика
                    return
            else:
                print("Войдите в аккаунт, чтобы смотреть видео")


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
#
# Примечания:
# Не забывайте для удобства использовать dunder(магические) методы: __str__, __repr__,
# __contains__, __eq__ и др. (повторить можно здесь)
# Чтобы не запутаться рекомендуется после реализации каждого метода проверять как он работает,
# тестировать разные вариации.
