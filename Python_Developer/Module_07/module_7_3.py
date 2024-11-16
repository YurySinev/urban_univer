class WordsFinder:
    all_words = {}

    def __init__(self, *files):
        self.file_names = self.files_to_list(files)  # обрабатываем список, затем присваиваем атрибуту

    # рекурсивная обработка списка файлов и приведение их к адекватному виду:
    def files_to_list(self, files) -> list:
        result_list = []
        for item in files:
            if isinstance(item, tuple) or isinstance(item, list):  # если внутри аргументов есть кортеж или список
                result_list.extend(self.files_to_list(item))  # персонально для них снова вызываем эту функцию
            else:
                if ',' in item:  # если два и более аргумента - одна строка
                    result_list.extend(item.split(', '))  # то разделяем ее на список и добавляем его
                else:
                    result_list.append(item)
        return result_list

    # удаление пунктуации из текста:
    def remove_punctuation(self, text):
        punctuation = [',', '.', '=', '!', '?', ';', ':']  # это надо удалить
        no_punctuation = ''.join(char for char in text if char not in punctuation)  # новая строка без пунктуации
        no_punctuation_list = no_punctuation.split()  # преобразуем ее в список
        for i in no_punctuation_list:  # проходимся по этому списку и
            if i == '-':  # отдельно проверяем, нет ли среди его элементов тире
                no_punctuation_list.remove(i)  # и удаляем, если есть
        return no_punctuation_list

    # получение списка всех слов из файлов:
    def get_all_words(self) -> dict:
        for file in self.file_names:
            with open(file) as f:  # открываем файл
                content = self.remove_punctuation(f.read())  # приводим его содержимое к списку слов
                self.all_words[file] = [word.lower() for word in content]  # добавляем этот список в словарь
        return self.all_words

    # поиск слова по всему словарю. Возвращает словарь {имя файла: порядковый номер слова}:
    def find(self, word) -> dict:
        result = {}
        for key, value in self.all_words.items():
            if word.lower() in value:
                result[key] = value.index(word.lower()) + 1
            else:
                return f'Ни хера нет такого слова'
        return result

    # сколько раз встречается слово? - {имя файла: сколько раз встречается}
    def count(self, word) -> dict:
        result = {}
        count = 0
        for key, value in self.all_words.items():
            for i in value:
                if word.lower() == i:
                    count += 1
                    result[key] = count
        return result


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# Вывод на консоль:
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его',
# 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}