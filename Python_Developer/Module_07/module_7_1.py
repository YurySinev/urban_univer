class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):  # считывает всю информацию из файла __file_name,
        # закрывает его и возвращает единую строку со всеми товарами из файла __file_name
        file = open(self.__file_name, 'r')
        file.seek(0)
        products_info = file.read()
        file.close()
        return products_info

    def add(self, *products):  # принимает неограниченное количество объектов
        # класса Product. Добавляет в файл __file_name каждый продукт из products, если его
        # ещё нет в файле (по названию). Если такой продукт уже есть, то не добавляет и
        # выводит строку 'Продукт <название> уже есть в магазине'
        file = open(self.__file_name, 'r+')
        content = file.read()
        file.seek(0)
        for i in products:
            if str(i) in content:
                print(f'Продукт {str(i)} уже есть в магазине')
            else:
                file.write(str(i) + '\n')
        file.close()


if __name__ == '__main__':
    # Пример результата выполнения программы:
    # Пример работы программы:
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())

# Вывод на консоль:

# Первый запуск:
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables

# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato, 50.5, Vegetables уже есть в магазине
# Продукт Spaghetti, 3.4, Groceries уже есть в магазине
# Продукт Potato, 5.5, Vegetables уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables

# Как выглядит файл после запусков:
#     Potato, 50.5, Vegetables
#     Spaghetti, 3.4, Groceries
#     Potato, 5.5, Vegetables
