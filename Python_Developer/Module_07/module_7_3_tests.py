from module_7_3 import WordsFinder

wf = WordsFinder('file1.txt, file2.txt', ['file3.txt', ('file4.txt', 'file5.txt, file6.txt')])
print(wf.file_names)
for i in wf.file_names:
    print(i)
finder2 = WordsFinder('test_file.txt', 'sample.txt', 'sample3.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.find('строка'))  # 7 слово по счёту
print(finder2.find('Бобик'))  #
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# with open('test_file_1252.txt') as f:
#     print(f.read())