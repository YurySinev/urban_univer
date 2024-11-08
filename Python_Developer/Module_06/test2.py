from module6hard import Figure, Circle, Cube, Triangle

__sides = 5
sides = 12, 13, 14, 15, 16
def is_valid(*sides):
    if len(sides) != __sides:
        return False
    for i in sides:
        if i <= 0 or not isinstance(i, int):
            return False
        else:
            continue
    return True

print(is_valid(*sides))

# for i in sides:
#     if i <= 0 or type(i) is not int:
#         print("NO")
#     else:
#         print('Yes')

print()
circle1 = Circle((125, 125, 125), 25)
cube1 = Cube((222, 35, 130), 6, 4, 5)
fig = Figure((255, 255, 255), 11, 23, 43, 21, 33)
triangle = Triangle((233, 232, 231), 33, 66, 55)