# абсолютный импорт:
# from Python_Developer.Module_04.package1.module1 import hello
# относительный импорт:
from .module1 import hello
# если отсутствует файл main.py с АБСОЛЮТНЫМ ПУТЕМ, то
# ImportError: attempted relative import with no known parent package
# файл запускается как main и он не знает, где он находится


def good_word(name):
    hello(name)
    print("Ты лучший, ", name)

if __name__ == '__main__':
    good_word("Урбан")

# good_word("Юрий")