class Human:
    def __init__(self, name="Имярек", age=30):
        self.name = name
        self.age = age
        self.self_info()

    def self_info(self):
        years = ""
        if self.age in [11, 111]:
            years = "лет"
        elif self.age % 10 in [5, 6, 7, 8, 9, 0]:
            years = "лет"
        elif self.age % 10 == 1:
            years = "год"
        else:
            years = "года"
        print(f"Привет! Меня зовут {self.name}. Мне {self.age} {years}.")

    def birthday(self):
        self.age += 1
        print(f"У меня день рождения. Теперь мне {self.age}.")
        self.self_info()


yury = Human("Юрий", 63)
diana = Human("Диана", 25)
elena = Human("Елена", 65)
elena.birthday()
