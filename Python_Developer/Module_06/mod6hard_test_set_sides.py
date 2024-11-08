from module6hard import Figure, Circle, Triangle, Cube

print()
circle1 = Circle((125, 125, 125), 25)
cube1 = Cube((222, 35, 130), 6)
fig = Figure((255, 255, 255), 11, 23, 43, 21, 33)
triangle = Triangle((233, 232, 231), 33, 66, 55)

print(circle1.get_sides())
circle1.set_sides(33)
print(circle1.get_sides())
print(cube1.get_sides())
cube1.set_sides(7)
print(cube1.get_sides())
print(fig.get_sides())
print(triangle.get_sides())
triangle.set_sides(25, 23, 47)
print(triangle.get_sides())
