class Human:
    head = True

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

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

    def __bool__(self):
        return bool(self.age)

    def __str__(self):
        return f'Имя: {self.name}. Возраст: {self.age}'

    # def __del__(self):
    #     print(f"{self.name} ушел...")


yury = Human("Юрий", 63)
diana = Human("Диана", 25)
elena = Human("Елена", 65)
# elena.birthday()
# diana.birthday()
# yury.birthday()
# print(len(diana))
# print(len(yury))
# print(yury > diana)
# print(diana == yury)
# if yury:
#     yury.self_info()
# if diana:
#     diana.self_info()
# if elena:
#     elena.self_info()
print(yury)
print(Human.head)
print(yury.head)
Human.head = False
print(Human.head)
print(yury.head)
print(diana.head)
igor = Human("Игорь", 50)
igor.head = True
print("Есть ли у Игоря голова? ", igor.head)