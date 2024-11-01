class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f'Привет, меня зовут {self.name}')


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()


student = Student('Юрий', 'Урбан', 'Питон 1')
print(Student.mro())
print(student.group)
student.about()
print()


def __is_valid_color(color):
    # проверяет корректность переданных значений перед установкой нового цвета.
    for i in color:
        if i < 0 or i > 255:
            return False
        else:
            continue
    return True


color = [28, 35, 77]
print(__is_valid_color(color))
