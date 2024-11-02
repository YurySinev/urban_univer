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