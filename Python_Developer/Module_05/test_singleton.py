class User:
    __instance = None  # Singleton Pattern

    def __new__(cls, *args, **kwargs):
        print("Я в нью")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print("Я в ините")
        self.args = args
        for k, v in kwargs.items():
            setattr(self, k, v)


other = [6, 3, 7, 8, 2, 9]
user = {'name': 'Юрий', 'age': 63, 'gender': 'male'}

yury = User(*other, **user)
print(yury.args)
print(yury.name, yury.age)
print(yury.gender)
