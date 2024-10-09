class User:
    def __new__(cls, *args, **kwargs):
        print("Я в нью")
        return cls.__init__(cls)
    def __init__(self):
        print("Я в ините")

user1 = User()
print(user1)