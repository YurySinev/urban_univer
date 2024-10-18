class Video:
    """
    Класс объектов видео: название, продолжительность, секунда остановки и возрастное ограничение
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title  # (заголовок, строка)
        self.duration = duration  # (продолжительность, секунды),
        self.time_now = time_now  # (секунда остановки (изначально 0)
        self.adult_mode = adult_mode  # (ограничение по возрасту bool (False по умолчанию))

    def __str__(self):
        return self.title


if __name__ == '__main__':
    # проверки и эксперименты
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    print(v1)
    print(v2)
    print(v1.__repr__())
    print(repr(v1))
    print(v1.__repr__()[0])  # получаем элементы по индексу
    print(repr(v1)[0])  #
    print(repr(v1))  # получаем элементы по индексу
    print(hash(v1))
