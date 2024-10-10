# class User:
#     def __new__(cls, *args, **kwargs):
#         print("Я в нью")
#         return cls.__init__(cls)
#
#     def __init__(self):
#         print("Я в ините")
#
#
# user1 = User()
# print(user1)


class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
        self.x = 15
        print(first)
        print(second)
        print(third)


data = [4, 7, 2, 4, 5, 8, 9, 1, 0, 5, 2]
dic = {'name': 'Yury', 'age': 63, 'gender': 'male', 'height': 182, 'weight': 81}
user = Example(10, 11,12)
ex = Example('data', second=25, third=3.14)