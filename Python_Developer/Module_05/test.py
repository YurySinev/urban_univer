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


# data = [4, 7, 2, 4, 5, 8, 9, 1, 0, 5, 2]
# dic = {'name': 'Yury', 'age': 63, 'gender': 'male', 'height': 182, 'weight': 81}
# user = Example(10, 11,12)
# ex = Example('data', second=25, third=3.14)

def check_password(pswd):
    symbols = [chr(i) for i in range(33, 48)]
    caps = [chr(i) for i in range(65,91)]
    nums = [i for i in range(0,10)]
    letters = [chr(i) for i in range(97, 123)]
    if any(c in pswd for c in symbols) and any(c in pswd for c in caps) and any(c in pswd for c in str(nums)):
        return True
    else:
        return False

# print("symbols: ", symbols)
# print(caps)
# print(nums)
# print(letters)

password = 'asdf1$D'
print(check_password(password))
